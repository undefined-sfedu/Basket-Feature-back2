from sqlalchemy.orm import Session
from app.core.models.possessions import Possessions
from app.core.schemas.possessions import PossessionsCreate


def get_possessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Possessions).offset(skip).limit(limit).all()


def get_possession(db: Session, possession_id: int):
    return db.query(Possessions).filter(Possessions.id == possession_id).first()


def create_possession(db: Session, possession: PossessionsCreate):
    db_possession = Possessions(**possession.dict())
    db.add(db_possession)
    db.commit()
    db.refresh(db_possession)
    return db_possession
