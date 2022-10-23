from sqlalchemy import Column, Integer, Identity, ARRAY
from sqlalchemy.orm import relationship

from app.core.database import Base


class Possessions(Base):
    __tablename__ = 'possessions'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    players_array = Column(ARRAY(Integer()), nullable=False)

    actions = relationship('Actions', back_populates='possession')