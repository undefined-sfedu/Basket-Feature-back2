from fastapi import Depends, APIRouter
from app.core.crud.player_operations import *
from app.core.schemas.player import Player as PlayerSchema
from app.core.dependencies import get_db

player_router = APIRouter(prefix="/players", tags=["players"])


@player_router.post("/create/{team_id}", response_model=PlayerSchema)
def create_player_for_team(team_id: int, player: PlayerCreate, db: Session = Depends(get_db)):
    return create_team_player(db, player, team_id)


@player_router.get("/get_all", response_model=list[PlayerSchema])
def get_all_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_players(db, skip=skip, limit=limit)


@player_router.get("/{user_id}", response_model=PlayerSchema)
def get_player_by_id(player_id: int, db: Session = Depends(get_db)):
    return get_player(db=db, player_id=player_id)
