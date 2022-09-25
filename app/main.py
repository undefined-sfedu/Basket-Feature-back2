from app.core import models
from app.core.database import engine
from fastapi import FastAPI
from app.api.endpoints.users import router as user_router

models.Base.metadata.create_all(bind=engine)

backend_app = FastAPI()

backend_app.include_router(user_router)
