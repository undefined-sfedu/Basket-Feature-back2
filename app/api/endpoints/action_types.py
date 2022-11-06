from fastapi import Depends, APIRouter
from app.core.crud.action_types_operations import *
from app.core.schemas.action_types import Throw as ThrowSchema, Faul as FaulSchema, Loss as LossSchema
from app.core.dependencies import get_db


action_types_router = APIRouter(prefix="/action_types", tags=["action_types"])


@action_types_router.post("/create_throw", response_model=ThrowSchema)
def create_throw(throw: ThrowCreate, db: Session = Depends(get_db)):
    return db_create_throw(db, throw)


@action_types_router.post("/create_loss", response_model=LossSchema)
def create_loss(loss: LossSchema, db: Session = Depends(get_db)):
    return db_create_loss(db, loss)


@action_types_router.post("/create_faul", response_model=FaulSchema)
def create_faul(faul: FaulCreate, db: Session = Depends(get_db)):
    return db_create_faul(db, faul)


@action_types_router.get("/get_all_throws", response_model=list[ThrowSchema])
def get_all_actions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db_get_throws(db, skip, limit)


@action_types_router.get("/get_all_losses", response_model=list[LossSchema])
def get_all_losses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db_get_losses(db, skip, limit)


@action_types_router.get("/get_all_fauls", response_model=list[FaulSchema])
def get_all_fauls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db_get_fauls(db, skip, limit)


@action_types_router.get("/get_throw/{throw_id}", response_model=ThrowSchema)
def get_throw_by_id(throw_id: int, db: Session = Depends(get_db)):
    return db_get_throw_by_id(db, throw_id)


@action_types_router.get("/get_loss/{loss_id}", response_model=LossSchema)
def get_loss_by_id(loss_id: int, db: Session = Depends(get_db)):
    return db_get_loss_by_id(db, loss_id)


@action_types_router.get("/get_faul/{faul_id}", response_model=FaulSchema)
def get_faul_by_id(faul_id: int, db: Session = Depends(get_db)):
    return db_get_faul_by_id(db, faul_id)
