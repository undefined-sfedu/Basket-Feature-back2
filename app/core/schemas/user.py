from pydantic import BaseModel

from app.core.schemas.team import Team


class UserBase(BaseModel):
    email: str
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    teams: list[Team] = []

    class Config:
        orm_mode = True
