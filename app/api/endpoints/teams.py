from fastapi import Depends, APIRouter
from app.core import crud, schemas
from sqlalchemy.orm import Session
from app.core.dependencies import get_db


team_router = APIRouter(prefix="/teams", tags=["teams"])


@team_router.get("/get_all", response_model=list[schemas.Team])
def get_all_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_teams(db, skip=skip, limit=limit)


@team_router.get("/{team_id}", response_model=list[schemas.Player])
def get_team_players(team_id: int, db: Session = Depends(get_db)):
    return crud.get_team(db, team_id=team_id).players


@team_router.post("/{team_id}/players", response_model=schemas.Player)
def create_player_for_team(team_id: int, player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_team_player(db, player, team_id)
