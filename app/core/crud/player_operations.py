from sqlalchemy.orm import Session
from app.core.models.player import Player
from app.core.schemas.player import PlayerCreate


def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Player).offset(skip).limit(limit).all()


def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()


def create_team_player(db: Session, player: PlayerCreate, team_id: int):
    db_player = Player(**player.dict(), team_id=team_id)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player
