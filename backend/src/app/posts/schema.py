from datetime import datetime
from typing import List, Optional, Dict, Any

from pydantic import BaseModel

from src.app.comments.schema import Comment
from src.app.user.schema import DisplayUser


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: DisplayUser
    comments: List[Comment]

    class Config:
        orm_mode = True
