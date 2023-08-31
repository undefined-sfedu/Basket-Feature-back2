from sqlalchemy.orm import Session
from core.models import Actions
from core.schemas.action import ActionCreate


def get_actions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Actions).offset(skip).limit(limit).all()


def get_action(db: Session, action_id: int):
    return db.query(Actions).filter(Actions.id == action_id).first()


def create_action(db: Session, action: ActionCreate):
    db_action = Actions(seconds=action.seconds,
                        time_type_id=action.time_type_id,
                        time_id=action.time_id,
                        possession_id=action.possession_id,
                        active_players_id=action.active_players_id,
                        start_attack_type_id=action.start_attack_type_id,
                        attack_type_id=action.attack_type_id,
                        throw_id=action.throw_id,
                        loss_id=action.loss_id,
                        faul_id=action.faul_id)
    db.add(db_action)
    db.commit()
    db.refresh(db_action)
    return db_action
