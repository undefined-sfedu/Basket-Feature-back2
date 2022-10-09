from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class ActivePlayer(Base):
    __tablename__ = "active_players"

    id = Column(Integer, primary_key=True, index=True)
    first_player = Column(Integer, nullable=False, ForeignKey("players.id"))
    second_player = Column(Integer, nullable=False, ForeignKey("players.id"))
    third_player = Column(Integer, nullable=False, ForeignKey("players.id"))
    fourth_player = Column(Integer, nullable=False, ForeignKey("players.id"))
    fifth_player = Column(Integer, nullable=False, ForeignKey("players.id"))

    player_1 = relationship("Player", foreign_keys=[first_player])
    player_2 = relationship("Player", foreign_keys=[second_player])
    player_3 = relationship("Player", foreign_keys=[third_player])
    player_4 = relationship("Player", foreign_keys=[fourth_player])
    player_5 = relationship("Player", foreign_keys=[fifth_player])
