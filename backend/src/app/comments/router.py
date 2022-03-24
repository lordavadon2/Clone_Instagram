from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.responses import Response

from src.app.auth.jwt import get_current_user
from src.db import db
from src.app.comments import schema, services, models

router = APIRouter()


@router.post('/add',
             status_code=status.HTTP_201_CREATED,
             response_model=schema.CommentResponse,
             dependencies=[Depends(get_current_user)])
def create_post(comment: schema.Comment, database: Session = Depends(db.get_db)) -> models.Comment:
    return services.create_comment(comment, database)


@router.get('/{post_id}/all',
            status_code=status.HTTP_200_OK,
            response_model=List[schema.CommentResponse])
def post_list(post_id: int, database: Session = Depends(db.get_db)) -> List[models.Comment]:
    return services.get_comments(post_id, database)
