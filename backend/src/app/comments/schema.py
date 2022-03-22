from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    text: str
    username: str
    post_id: int


class CommentResponse(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True
