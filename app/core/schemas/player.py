from pydantic import BaseModel


class PlayerBase(BaseModel):
    number: int


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    team_id: int

    class Config:
        orm_mode = True
