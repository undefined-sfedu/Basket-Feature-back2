from sqlalchemy import Integer, String, Column, ForeignKey, Identity
from sqlalchemy.orm import relationship
from app.core.database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    name = Column(String(100), nullable=False)
    user_id = Column(ForeignKey('users.id'))

    user = relationship("User", back_populates="teams")
    players = relationship("Player", back_populates="team")
