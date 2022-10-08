from sqlalchemy import Integer, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    team_a_id = Column(Integer, ForeignKey("teams.id"))
    team_b_id = Column(Integer, ForeignKey("teams.id"))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="games")
    team_a = relationship("Team", back_populates="games")
    team_b = relationship("Team", back_populates="games")
