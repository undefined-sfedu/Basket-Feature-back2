from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class TeamBase(BaseModel):
    name: str


class TeamCreate(TeamBase):
    pass


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


class Team(TeamBase):
    id: int
    user_id: int
    players: list[Player] = []

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    teams: list[Team] = []

    class Config:
        orm_mode = True
