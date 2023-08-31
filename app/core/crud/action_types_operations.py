from sqlalchemy.orm import Session
from core.models import Throws, LossDict, Fauls
from core.schemas.action_types import ThrowCreate, FaulCreate, Loss


def db_create_throw(db: Session, throw: ThrowCreate):
    db_throw = Throws(**throw.dict())
    db.add(db_throw)
    db.commit()
    db.refresh(db_throw)
    return db_throw


def db_create_loss(db: Session, loss: Loss):
    db_loss = LossDict(**loss.dict())
    db.add(db_loss)
    db.commit()
    db.refresh(db_loss)
    return db_loss


def db_create_faul(db: Session, faul: FaulCreate):
    db_faul = LossDict(**faul.dict())
    db.add(db_faul)
    db.commit()
    db.refresh(db_faul)
    return db_faul


def db_get_throws(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Throws).offset(skip).limit(limit).all()


def db_get_losses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LossDict).offset(skip).limit(limit).all()


def db_get_fauls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Fauls).offset(skip).limit(limit).all()


def db_get_faul_by_id(db: Session, faul_id: int):
    return db.query(Fauls).filter(Fauls.id == faul_id).first()


def db_get_throw_by_id(db: Session, throw_id: int):
    return db.query(Throws).filter(Throws.id == throw_id).first()


def db_get_loss_by_id(db: Session, loss_id: int):
    return db.query(LossDict).filter(LossDict.id == loss_id).first()

