from sqlalchemy import Integer, String, Column, Identity, CHAR
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    email = Column(String(64), nullable=False)
    pass_hash = Column(CHAR(64), nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    middle_name = Column(String(30))

    teams = relationship("Team", back_populates="user")
    games = relationship("Game", back_populates="user")
