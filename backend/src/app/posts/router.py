from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session
from starlette.responses import Response

from src.app.auth.jwt import get_current_user
from src.db import db
from src.app.posts import schema, services, models
from src.app.user import models as user_model

router = APIRouter()


@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=schema.PostDisplay)
def create_post(post: schema.PostBase, database: Session = Depends(db.get_db),
                user: user_model.User = Depends(get_current_user)) -> models.Post:
    return services.create_post(post, user, database)


@router.get('/all',
            status_code=status.HTTP_200_OK,
            response_model=List[schema.PostDisplay])
def post_list(database: Session = Depends(db.get_db)) -> List[models.Post]:
    return services.get_posts(database)


@router.post('/image',
             dependencies=[Depends(get_current_user)])
def upload_image(image: UploadFile = File(...)) -> dict:
    path = services.upload_img(image)
    return {'filename': path}


@router.delete('/{post_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response,
               dependencies=[Depends(get_current_user)])
def delete_post(post_id: int, database: Session = Depends(db.get_db)):
    return services.delete_post(post_id, database)
