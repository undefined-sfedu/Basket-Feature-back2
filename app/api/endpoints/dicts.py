from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.crud.dicts_operations import get_loss_dict, get_faul_dict, get_time_dict, get_result_dict, \
    get_time_type_dict, get_play_type_dict, get_attack_type_dict, get_start_attack_dict
from core.schemas.dicts import *
from core.schemas.action_types import Loss
from core.dependencies import get_db


dicts_router = APIRouter(prefix="/dicts", tags=["dicts"])


@dicts_router.get("/get_loss", response_model=list[Loss])
def get_loss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_loss_dict(db=db, skip=skip, limit=limit)


@dicts_router.get("/get_time", response_model=list[TimeType])
def get_time(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_time_dict(db=db, skip=skip, limit=limit)


@dicts_router.get("/get_time_type", response_model=list[TimeTypeDict])
def get_time_type(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_time_type_dict(db=db, skip=skip, limit=limit)


@dicts_router.get("/get_result", response_model=list[ResultType])
def get_result(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_result_dict(db=db, skip=skip, limit=limit)


@dicts_router.get("/get_play_type", response_model=list[PlayType])
def get_play_type(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_play_type_dict(db=db, skip=skip, limit=limit)


@dicts_router.get("/get_faul", response_model=list[FaulType])
def get_faul(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_faul_dict(db=db, skip=skip, limit=limit)


@dicts_router.get("/get_start_attack", response_model=list[StartAttackType])
def get_start_attack(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_start_attack_dict(db=db, skip=skip, limit=limit)


@dicts_router.get("/get_attack_type", response_model=list[AttackType])
def get_attack_type(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_attack_type_dict(db=db, skip=skip, limit=limit)
