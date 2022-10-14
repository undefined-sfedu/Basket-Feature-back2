from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class ActivePlayer(Base):
    __tablename__ = "active_players"

    id = Column(Integer, primary_key=True, index=True)
    first_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    second_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    third_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    fourth_player = Column(Integer, ForeignKey("players.id"), nullable=False)
    fifth_player = Column(Integer, ForeignKey("players.id"), nullable=False)

    player_1 = relationship("Player", foreign_keys=[first_player])
    player_2 = relationship("Player", foreign_keys=[second_player])
    player_3 = relationship("Player", foreign_keys=[third_player])
    player_4 = relationship("Player", foreign_keys=[fourth_player])
    player_5 = relationship("Player", foreign_keys=[fifth_player])
