from app.core import models
from app.core.database import engine
from fastapi import FastAPI
from app.api.endpoints.users import user_router
from app.api.endpoints.teams import team_router
from app.api.endpoints.players import player_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(team_router)
app.include_router(player_router)
