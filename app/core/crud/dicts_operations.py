from sqlalchemy.orm import Session
from core.models import LossDict, TimeDict, TimeTypeDict, ResultDict, PlayTypeDict, StartAttackDict, FaulTypes, \
    AttackTypes


def get_loss_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LossDict).offset(skip).limit(limit).all()


def get_time_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TimeDict).offset(skip).limit(limit).all()


def get_time_type_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TimeTypeDict).offset(skip).limit(limit).all()


def get_result_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ResultDict).offset(skip).limit(limit).all()


def get_play_type_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PlayTypeDict).offset(skip).limit(limit).all()


def get_start_attack_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(StartAttackDict).offset(skip).limit(limit).all()


def get_faul_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FaulTypes).offset(skip).limit(limit).all()


def get_attack_type_dict(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AttackTypes).offset(skip).limit(limit).all()
