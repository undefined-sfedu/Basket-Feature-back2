from fastapi import Depends, APIRouter

from app.core.crud.player_operations import create_team_player
from app.core.crud.team_operations import *
from app.core.dependencies import get_db
from app.core.schemas.player import PlayerCreate, Player
from app.core.schemas.team import Team as TeamSchema

team_router = APIRouter(prefix="/teams", tags=["teams"])


@team_router.get("/get_all", response_model=list[TeamSchema])
def get_all_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_teams(db, skip=skip, limit=limit)


@team_router.get("/{team_id}", response_model=list[Player])
def get_team_players(team_id: int, db: Session = Depends(get_db)):
    return get_team(db, team_id=team_id).players


@team_router.post("/{team_id}/players", response_model=Player)
def create_player_for_team(team_id: int, player: PlayerCreate, db: Session = Depends(get_db)):
    return create_team_player(db, player, team_id)
