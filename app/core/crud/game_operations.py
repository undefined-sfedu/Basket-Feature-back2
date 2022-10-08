from sqlalchemy.orm import Session
from app.core.models.game import Game
from app.core.schemas.game import GameCreate


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Game).offset(skip).limit(limit).all()


def get_game(db: Session, game_id: int):
    return db.query(Game).filter(Game.id == game_id).first()


def get_game_by_user(db: Session, user_id: int):
    return db.query(Game).filter(Game.user_id == user_id).all()


def create_game(db: Session, game: GameCreate, user_id: int):
    db_game = Game(**game.dict(), user_id=user_id)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
