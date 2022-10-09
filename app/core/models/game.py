from sqlalchemy import Integer, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    team_a_id = Column(Integer, nullable=False, ForeignKey("teams.id"))
    team_b_id = Column(Integer, nullable=False, ForeignKey("teams.id"))
    date = Column(DateTime)
    user_id = Column(Integer, nullable=False, ForeignKey("users.id"))

    user = relationship("User", back_populates="games")
    team_a = relationship("Team", foreign_keys=[team_a_id])
    team_b = relationship("Team", foreign_keys=[team_b_id])
