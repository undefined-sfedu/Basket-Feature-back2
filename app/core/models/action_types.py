from sqlalchemy import Integer, Column, ForeignKey, text, SmallInteger, Identity, Boolean, CHAR, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Throw(Base):
    __tablename__ = 'throws'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    play_type_id = Column(ForeignKey('play_type_dict.id'), nullable=False)
    zone = Column(SmallInteger, nullable=False)
    result_id = Column(ForeignKey('result_dict.id'), nullable=False)
    is_assist = Column(Boolean, nullable=False, server_default=text('false'))

    play_type = relationship('PlayTypeDict')
    result = relationship('ResultDict')
    actions = relationship('Action', back_populates='throw')


class Fauls(Base):
    __tablename__ = 'fauls'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    faul_type_id = Column(ForeignKey('faul_types.id'), nullable=False)
    scored = Column(SmallInteger, nullable=False, server_default=text('0'))

    faul_type = relationship('FaulTypes', back_populates='fauls')
    actions = relationship('Actions', back_populates='faul')


class LossDict(Base):
    __tablename__ = 'loss_dict'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    abbreviate = Column(CHAR(3), nullable=False)
    description = Column(String(30), server_default=text('NULL::character varying'))

    actions = relationship('Action', back_populates='loss')
