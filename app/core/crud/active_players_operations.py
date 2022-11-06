from sqlalchemy.orm import Session
from app.core.models import ActivePlayers
from app.core.schemas.active_players import ActivePlayersCreate


def get_active_players(db: Session, active_players_id: int):
    return db.query(ActivePlayers).filter(ActivePlayers.id == active_players_id).first()


def create_active_players(db: Session, active_players: ActivePlayersCreate):
    db_active_players = ActivePlayers(**active_players.dict())
    db.add(db_active_players)
    db.commit()
    db.refresh(db_active_players)
    return db_active_players
