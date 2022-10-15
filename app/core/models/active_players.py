from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class ActivePlayers(Base):
    __tablename__ = "active_players"

    id = Column(Integer, primary_key=True, index=True)
    first_player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    second_player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    third_player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    fourth_player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    fifth_player_id = Column(Integer, ForeignKey("players.id"), nullable=False)

    first_player = relationship("Player", foreign_keys=[first_player_id])
    second_player = relationship("Player", foreign_keys=[second_player_id])
    third_player = relationship("Player", foreign_keys=[third_player_id])
    fourth_player = relationship("Player", foreign_keys=[fourth_player_id])
    fifth_player = relationship("Player", foreign_keys=[fifth_player_id])
