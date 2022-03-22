from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from src.db.db import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime, default=datetime.now)

    post_id = Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"), )
    post = relationship("Post", back_populates="comments")
