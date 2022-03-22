from __future__ import annotations

from sqlalchemy.orm import Session

from src.app.user import models


def verify_email_exist(email: str, db_session: Session) -> models.User | None:
    return db_session.query(models.User).filter(models.User.email == email).first()
