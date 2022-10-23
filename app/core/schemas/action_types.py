from pydantic import BaseModel

from app.core.schemas.dicts import PlayTypes, ResultTypes, FaulTypes, Dictionary


class ThrowCreate(BaseModel):
    play_type_id: int
    zone: int
    result_id: int
    is_assist: bool


class Throw(ThrowCreate):
    id: int

    play_type: PlayTypes
    result: ResultTypes

    class Config:
        orm_mode = True


class FaulCreate(BaseModel):
    faul_type_id: int
    scored: int


class Faul(FaulCreate):
    id: int

    faul_type: FaulTypes

    class Config:
        orm_mode = True


class Loss(Dictionary):
    pass
