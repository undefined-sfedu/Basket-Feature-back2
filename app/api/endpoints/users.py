from fastapi import Depends, HTTPException, APIRouter
import hashlib

from sqlalchemy.orm import Session

from app.core.crud.user_operations import get_user, get_users, get_user_by_email, create_user as db_create_user
from app.core.schemas.user import User as UserSchema, UserCreate
from app.core.schemas.team import Team as TeamSchema
from app.core.dependencies import get_db

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/create", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_create_user(db=db, user=user)


@user_router.get("/get_all", response_model=list[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.get("/get_by_email/{user_email}", response_model=UserSchema)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.get("/auth/{email}/{password}", response_model=UserSchema)
def auth_user(email: str, password: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=email)
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.pass_hash != hashed_pass:
        raise HTTPException(status_code=401, detail="Wrong password")

    return db_user


@user_router.get("/{user_id}", response_model=list[TeamSchema])
def get_user_teams(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id).teams
