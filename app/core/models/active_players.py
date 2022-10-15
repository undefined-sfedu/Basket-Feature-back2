from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class ActivePlayers(Base):
    __tablename__ = "active_players"

    id = Column(Integer, primary_key=True, index=True)
    first_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    second_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    third_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    fourth_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    fifth_player = Column(Integer, ForeignKey("players.id"), nullable=False)

    active_players = relationship(
        "Player",
        foreign_keys=[first_player, second_player, third_player, fourth_player, fifth_player]
    )
