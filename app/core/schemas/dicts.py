from pydantic import BaseModel


class Dictionary(BaseModel):
    id: int
    abbreviate: str
    description: str

    class Config:
        orm_mode = True


class TimeTypeDict(BaseModel):
    id: int
    time_type: str

    class Config:
        orm_mode = True


class AttackTypes(Dictionary):
    pass


class StartAttackTypes(Dictionary):
    pass


class FaulTypes(Dictionary):
    pass


class PlayTypes(Dictionary):
    pass


class ResultTypes(Dictionary):
    pass


class TimeTypes(Dictionary):
    id: int
    time: str

    class Config:
        orm_mode = True
