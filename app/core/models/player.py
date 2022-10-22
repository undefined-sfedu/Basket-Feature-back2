from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False, default=1)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    team = relationship("Team", back_populates="players")
