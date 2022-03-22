import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from src.db.db import Base
from . import hashing


class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()), index=True)
    username = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))

    posts = relationship("Post", back_populates="user")

    def __init__(self, username, email, password, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)
