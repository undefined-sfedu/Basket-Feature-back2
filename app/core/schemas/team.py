from pydantic import BaseModel

from app.core.schemas.player import Player


class TeamBase(BaseModel):
    name: str


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int
    user_id: int
    players: list[Player] = []

    class Config:
        orm_mode = True
