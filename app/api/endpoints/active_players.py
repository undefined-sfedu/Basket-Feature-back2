from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from core.crud.active_players_operations import create_active_players as db_create_active_players
from core.crud.active_players_operations import get_active_players as db_get_active_players
from core.schemas.active_players import ActivePlayers as ActivePlayersSchema, ActivePlayersCreate
from core.dependencies import get_db

active_players_router = APIRouter(prefix="/active_players", tags=["active_players"])


@active_players_router.post("/create", response_model=ActivePlayersSchema)
def create_active_players(active_players: ActivePlayersCreate, db: Session = Depends(get_db)):
    return db_create_active_players(db, active_players)


@active_players_router.get("/{active_players_id}", response_model=ActivePlayersSchema)
def get_active_players(active_players_id: int, db: Session = Depends(get_db)):
    return db_get_active_players(db, active_players_id)
