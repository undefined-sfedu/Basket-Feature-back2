from fastapi import Depends, APIRouter
from app.core import crud, schemas
from sqlalchemy.orm import Session
from app.core.dependencies import get_db


player_router = APIRouter(prefix="/players", tags=["players"])


@player_router.get("/get_all", response_model=list[schemas.Player])
def get_all_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_players(db, skip=skip, limit=limit)
