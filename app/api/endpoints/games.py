from fastapi import Depends, APIRouter
from app.core.crud.game_operations import *
from app.core.schemas.game import Game as GameSchema
from app.core.dependencies import get_db

games_router = APIRouter(prefix="/games", tags=["games"])


@games_router.post("/create/{user_id}", response_model=GameSchema)
def create(game: GameCreate, user_id: int, db: Session = Depends(get_db)):
    return create_game(db, game, user_id)


@games_router.get("/get_all", response_model=list[GameSchema])
def get_all_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_games(db=db, skip=skip, limit=limit)


@games_router.get("/{game_id}", response_model=GameSchema)
def get_game_by_id(game_id: int, db: Session = Depends(get_db)):
    return get_game(db, game_id)


@games_router.get("/user/{user_id}", response_model=list[GameSchema])
def get_user_games(user_id: int, db: Session = Depends(get_db)):
    return get_game_by_user(db, user_id)
