from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    username: constr(min_length=2, max_length=50)


class BaseUser(User):
    email: EmailStr
    password: str


class DisplayUser(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
