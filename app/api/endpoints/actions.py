from fastapi import Depends, APIRouter
from core.crud.action_operations import *
from core.schemas.action import Action as ActionSchema
from core.dependencies import get_db


actions_router = APIRouter(prefix="/actions", tags=["actions"])


@actions_router.post("/create", response_model=ActionSchema)
def create(action: ActionCreate, db: Session = Depends(get_db)):
    return create_action(db, action)


@actions_router.get("/get_all", response_model=list[ActionSchema])
def get_all_actions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    response = get_actions(db, skip=skip, limit=limit)
    return response


@actions_router.get("/{action_id}", response_model=ActionSchema)
def get_action_by_id(action_id: int, db: Session = Depends(get_db)):
    return get_action(db=db, action_id=action_id)
