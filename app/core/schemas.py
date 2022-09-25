from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    first_name: str | None
    last_name: str | None
    middle_name: str | None

    class Config:
        orm_mode = True
