from pydantic import BaseModel

from core.schemas.active_players import ActivePlayers
from core.schemas.dicts import TimeType, TimeTypeDict, StartAttackType, AttackType
from core.schemas.action_types import Faul, Throw, Loss
from core.schemas.possessions import Possessions


class ActionBase(BaseModel):
    game_id: int | None
    seconds: int
    time_type_id: int
    time_id: int
    possession_id: int
    active_players_id: int
    start_attack_type_id: int
    attack_type_id: int
    throw_id: int | None = None
    loss_id: int | None = None
    faul_id: int | None = None


class ActionCreate(ActionBase):
    pass


class Action(ActionBase):
    id: int

    time: TimeType
    time_type: TimeTypeDict
    active_players: ActivePlayers
    possession: Possessions
    start_attack_type: StartAttackType
    attack_type: AttackType

    throw: Throw | None = None
    loss: Loss | None = None
    faul: Faul | None = None

    class Config:
        orm_mode = True
