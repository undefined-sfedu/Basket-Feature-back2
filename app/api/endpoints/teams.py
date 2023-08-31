from fastapi import Depends, APIRouter

from core.crud.team_operations import *
from core.dependencies import get_db
from core.schemas.player import Player as PlayerSchema
from core.schemas.team import Team as TeamSchema

team_router = APIRouter(prefix="/teams", tags=["teams"])


@team_router.post("/create/{user_id}", response_model=TeamSchema)
def create_team_for_user(
    user_id: int, team: TeamCreate, db: Session = Depends(get_db)
):
    return create_user_team(db=db, team=team, user_id=user_id)


@team_router.get("/get_all", response_model=list[TeamSchema])
def get_all_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_teams(db, skip=skip, limit=limit)


@team_router.get("/{team_id}", response_model=list[PlayerSchema])
def get_team_players(team_id: int, db: Session = Depends(get_db)):
    return get_team(db, team_id=team_id).players
