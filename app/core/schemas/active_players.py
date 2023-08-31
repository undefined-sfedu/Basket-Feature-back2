from pydantic import BaseModel

from core.schemas.player import Player


class ActivePlayersBase(BaseModel):
    pass


class ActivePlayersCreate(ActivePlayersBase):
    first_player_id: int
    second_player_id: int
    third_player_id: int
    fourth_player_id: int
    fifth_player_id: int


class ActivePlayers(ActivePlayersBase):
    id: int

    first_player: Player
    second_player: Player
    third_player: Player
    fourth_player: Player
    fifth_player: Player

    class Config:
        orm_mode = True
