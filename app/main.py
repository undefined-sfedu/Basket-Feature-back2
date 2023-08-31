import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints.action_types import action_types_router
from api.endpoints.actions import actions_router
from api.endpoints.dicts import dicts_router
from api.endpoints.games import games_router
from core.database import Base
from core.database import engine
from api.endpoints.users import user_router
from api.endpoints.teams import team_router
from api.endpoints.players import player_router
from api.endpoints.active_players import active_players_router
from api.endpoints.possessions import possessions_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(team_router)
app.include_router(player_router)
app.include_router(games_router)
app.include_router(active_players_router)
app.include_router(possessions_router)
app.include_router(action_types_router)
app.include_router(actions_router)
app.include_router(dicts_router)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
