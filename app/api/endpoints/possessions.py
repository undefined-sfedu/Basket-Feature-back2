from fastapi import Depends, APIRouter
from app.core.crud.possessions_operations import *
from app.core.schemas.possessions import Possessions as PossessionsSchema
from app.core.dependencies import get_db

possessions_router = APIRouter(prefix="/possessions", tags=["possessions"])


@possessions_router.post("/create", response_model=PossessionsSchema)
def create(possession: PossessionsCreate, db: Session = Depends(get_db)):
    return create_possession(db, possession)


@possessions_router.get("/get_all", response_model=list[PossessionsSchema])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_possessions(db=db, skip=skip, limit=limit)


@possessions_router.get("/{possession_id}", response_model=PossessionsSchema)
def get_possession_by_id(possession_id: int, db: Session = Depends(get_db)):
    return get_possession(db=db, possession_id=possession_id)
