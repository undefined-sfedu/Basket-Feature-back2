from pydantic import BaseModel

from app.core.schemas.active_players import ActivePlayers
from app.core.schemas.dicts import TimeTypes, TimeTypeDict, StartAttackTypes, AttackTypes
from app.core.schemas.action_types import Faul, Throw, Loss
from app.core.schemas.possessions import Possessions


class ActionBase(BaseModel):
    seconds: int


class ActionCreate(ActionBase):
    time_type_id: int
    time_id: int
    possession_id: int
    active_players_id: int
    start_attack_type_id: int
    attack_type_id: int
    throw_id: int | None = None
    loss_id: int | None = None
    faul_id: int | None = None


class Action(ActionBase):
    id: int

    time: TimeTypes
    time_type: TimeTypeDict
    active_players: ActivePlayers
    possession: Possessions
    start_attack_type: StartAttackTypes
    attack_type: AttackTypes

    throw: Throw | None = None
    loss: Loss | None = None
    faul: Faul | None = None
