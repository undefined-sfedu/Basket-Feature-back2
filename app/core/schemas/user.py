from pydantic import BaseModel

from app.core.schemas.team import Team


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    teams: list[Team] = []

    class Config:
        orm_mode = True
