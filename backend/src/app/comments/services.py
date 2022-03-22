from typing import List

from sqlalchemy.orm import Session

from src.app.comments import schema, models

image_url_types = ('absolute', 'relative')


def create_comment(comment: schema.Comment, db_session: Session) -> models.Comment:
    my_comment = models.Comment(**comment.dict())
    db_session.add(my_comment)
    db_session.commit()
    db_session.refresh(my_comment)
    return my_comment


def get_comments(post_id: int, db_session: Session) -> List[models.Comment]:
    return db_session.query(models.Comment).filter_by(post_id=post_id).all()

