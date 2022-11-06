from datetime import datetime

from pydantic import BaseModel

from app.core.schemas.action import Action
from app.core.schemas.active_players import ActivePlayers
from app.core.schemas.team import Team


class GameBase(BaseModel):
    team_a_id: int
    team_b_id: int
    start_five_id: int
    date: datetime | None = None


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    user_id: int

    team_a: Team
    team_b: Team
    start_five: ActivePlayers

    actions: list[Action] = []

    class Config:
        orm_mode = True
