from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from src.db.db import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime, default=datetime.now)

    user_id = Column(String, ForeignKey('users.id', ondelete="CASCADE"), )
    user = relationship("User", back_populates="posts")

    comments = relationship("Comment", back_populates="post")
