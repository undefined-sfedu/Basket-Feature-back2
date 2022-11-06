from pydantic import BaseModel


class PossessionsBase(BaseModel):
    players_array: list[int]


class PossessionsCreate(PossessionsBase):
    pass


class Possessions(PossessionsBase):
    id: int

    class Config:
        orm_mode = True
