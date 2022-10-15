from pydantic import BaseModel

from app.core.schemas.player import Player


class ActivePlayers(BaseModel):
    id: int

    first_player: int
    second_player: int
    third_player: int
    fourth_player: int
    fifth_player: int

    players: list[Player] = []

    class Config:
        orm_mode = True
