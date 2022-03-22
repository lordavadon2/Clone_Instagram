from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.db import db
from src.app.user import schema, validator, services, models

router = APIRouter()


@router.post('/create',
             status_code=status.HTTP_201_CREATED,
             response_model=schema.DisplayUser)
def create_user(request: schema.BaseUser,
                database: Session = Depends(db.get_db)) -> models.User:
    user = validator.verify_email_exist(request.email, database)
    if user:
        raise HTTPException(
            status_code=400,
            detail='The user with this email already exists.'
        )
    new_user = services.create_user(request, database)
    return new_user
