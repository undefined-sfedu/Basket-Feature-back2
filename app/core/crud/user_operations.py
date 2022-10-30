import hashlib
from sqlalchemy.orm import Session
from app.core.models import Users
from app.core.schemas.user import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()

    db_user = Users(
        email=user.email,
        pass_hash=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
