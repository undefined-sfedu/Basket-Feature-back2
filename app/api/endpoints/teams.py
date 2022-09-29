from fastapi import Depends, APIRouter
from app.core import crud, schemas
from sqlalchemy.orm import Session
from app.core.dependencies import get_db


teams_router = APIRouter(prefix="/teams", tags=["teams"])


@teams_router.get("/get_all", response_model=list[schemas.Team])
def get_all_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams


@teams_router.get("/{user_id}", response_model=list[schemas.Team])
def get_user_teams(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id).teams
