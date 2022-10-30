from sqlalchemy.orm import Session
from app.core.models import Teams
from app.core.schemas.team import TeamCreate


def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Teams).offset(skip).limit(limit).all()


def get_team(db: Session, team_id: int):
    return db.query(Teams).filter(Teams.id == team_id).first()


def create_user_team(db: Session, team: TeamCreate, user_id: int):
    db_team = Teams(**team.dict(), user_id=user_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
