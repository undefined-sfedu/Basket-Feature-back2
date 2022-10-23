from pydantic import BaseModel


class Dictionary(BaseModel):
    id: int
    abbreviate: str
    description: str


class TimeTypeDict(Dictionary):
    pass


class AttackTypes(Dictionary):
    pass


class FaulTypes(Dictionary):
    pass


class PlayTypes(Dictionary):
    pass


class ResultTypes(Dictionary):
    pass


class TimeTypes(Dictionary):
    pass
