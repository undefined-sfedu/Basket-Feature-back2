import hashlib

from fastapi import Depends, HTTPException, APIRouter
from app.core import crud, schemas
from sqlalchemy.orm import Session
from app.core.dependencies import get_db

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@user_router.get("/get_all", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.get("/{user_email}", response_model=schemas.User)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.get("/auth/{email}/{password}", response_model=schemas.User)
def auth_user(email: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.pass_hash != hashed_pass:
        raise HTTPException(status_code=401, detail="Wrong password")

    return db_user


@user_router.post("/{user_id}/teams/", response_model=schemas.Team)
def create_team_for_user(
    user_id: int, team: schemas.TeamCreate, db: Session = Depends(get_db)
):
    return crud.create_user_team(db=db, team=team, user_id=user_id)
