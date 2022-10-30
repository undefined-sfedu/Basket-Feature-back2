from fastapi import Depends, APIRouter
from app.core.crud.action_operations import *
from app.core.schemas.action import Action as ActionSchema
from app.core.dependencies import get_db


actions_router = APIRouter(prefix="/actions", tags=["actions"])


@actions_router.post("/create", response_model=ActionSchema)
def create(action: ActionCreate, db: Session = Depends(get_db)):
    return create_action(db, action)


@actions_router.get("/get_all", response_model=list[ActionSchema])
def get_all_actions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_actions(db, skip=skip, limit=limit)


@actions_router.get("/{action_id}", response_model=ActionSchema)
def get_action_by_id(action_id: int, db: Session = Depends(get_db)):
    return get_action(db=db, action_id=action_id)
