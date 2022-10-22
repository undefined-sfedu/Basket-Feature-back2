from sqlalchemy import Integer, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    team_a_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team_b_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_five_id = Column(Integer, ForeignKey("active_players.id"), nullable=False)

    user = relationship("User", back_populates="games")
    team_a = relationship("Team", foreign_keys=[team_a_id])
    team_b = relationship("Team", foreign_keys=[team_b_id])
    start_five = relationship("ActivePlayers", foreign_keys=[start_five_id])
