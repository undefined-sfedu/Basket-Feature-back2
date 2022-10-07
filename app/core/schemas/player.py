from pydantic import BaseModel


class PlayerBase(BaseModel):
    number: int
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int
    team_id: int

    class Config:
        orm_mode = True
