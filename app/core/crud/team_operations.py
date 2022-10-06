from sqlalchemy.orm import Session
from app.core.models.team import Team
from app.core.schemas.team import TeamCreate


def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Team).offset(skip).limit(limit).all()


def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()


def create_user_team(db: Session, team: TeamCreate, user_id: int):
    db_team = Team(**team.dict(), user_id=user_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
