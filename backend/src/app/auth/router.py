from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.app.auth import schema
from src.app.auth.jwt import create_access_token
from src.db import db
from src.app.user import models, hashing

router = APIRouter()


@router.post('/login', response_model=schema.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(db.get_db)):
    user = database.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username}
