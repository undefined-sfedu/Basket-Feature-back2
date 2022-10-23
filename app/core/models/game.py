from sqlalchemy import Integer, DateTime, Column, ForeignKey, Identity
from sqlalchemy.orm import relationship
from app.core.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    team_a_id = Column(ForeignKey('teams.id'), nullable=False)
    team_b_id = Column(ForeignKey('teams.id'), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    start_five_id = Column(ForeignKey('active_players.id'), nullable=False)
    date = Column(DateTime)

    user = relationship("User", back_populates="games")
    team_a = relationship("Team", foreign_keys=[team_a_id])
    team_b = relationship("Team", foreign_keys=[team_b_id])
    start_five = relationship("ActivePlayers", foreign_keys=[start_five_id])
