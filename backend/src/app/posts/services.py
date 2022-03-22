import random
import shutil
import string
from typing import List

from fastapi import HTTPException, status, UploadFile
from sqlalchemy.orm import Session

from src.app.posts import schema, models
from src.app.user import models as user_model

image_url_types = ('absolute', 'relative')


def create_post(post: schema.PostBase, user: user_model.User, db_session: Session) -> models.Post:
    if post.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Parameter image_url_type can only take values "absolute" or "relative".')
    my_post = models.Post(**post.dict(), user_id=user.id)
    db_session.add(my_post)
    db_session.commit()
    db_session.refresh(my_post)
    return my_post


def get_posts(db_session: Session) -> List[models.Post]:
    return db_session.query(models.Post).all()


def upload_img(image: UploadFile) -> str:
    rand_str = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return path


def delete_post(post_id: int, db_session: Session):
    db_session.query(models.Post).filter(models.Post.id == post_id).delete()
    db_session.commit()
