from __future__ import annotations

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.app.user import models, schema


def create_user(request: schema.BaseUser, db_session: Session) -> models.User:
    new_user = models.User(**request.dict())
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user


def get_user_by_id(user_id: int, db_session: Session) -> models.User:
    user_info = db_session.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found!")
    return user_info
