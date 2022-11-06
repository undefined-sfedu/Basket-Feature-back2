from pydantic import BaseModel


class Dictionary(BaseModel):
    id: int
    abbreviate: str
    description: str

    class Config:
        orm_mode = True


class TimeTypeDict(BaseModel):
    id: int
    time_type: int

    class Config:
        orm_mode = True


class AttackType(Dictionary):
    pass


class StartAttackType(Dictionary):
    pass


class FaulType(Dictionary):
    pass


class PlayType(Dictionary):
    pass


class ResultType(Dictionary):
    pass


class TimeType(BaseModel):
    id: int
    time: str

    class Config:
        orm_mode = True
