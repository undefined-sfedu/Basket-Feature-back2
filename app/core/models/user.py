from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    pass_hash = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)

    teams = relationship("Team", back_populates="user")
    games = relationship("Game", back_populates="user")
