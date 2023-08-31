from pydantic import BaseModel

from core.schemas.dicts import PlayType, ResultType, FaulType, Dictionary


class ThrowCreate(BaseModel):
    play_type_id: int
    zone: int
    result_id: int
    is_assist: bool


class Throw(ThrowCreate):
    id: int

    play_type: PlayType
    result: ResultType

    class Config:
        orm_mode = True


class FaulCreate(BaseModel):
    faul_type_id: int
    scored: int


class Faul(FaulCreate):
    id: int

    faul_type: FaulType

    class Config:
        orm_mode = True


class Loss(Dictionary):
    pass
