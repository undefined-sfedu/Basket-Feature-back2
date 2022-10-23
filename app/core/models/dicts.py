from sqlalchemy import Integer, String, Column, Identity, CHAR, SmallInteger, text
from sqlalchemy.dialects.postgresql import INT4RANGE
from sqlalchemy.orm import relationship
from app.core.database import Base


class AttackTypes(Base):
    __tablename__ = 'attack_types'

    id = Column(SmallInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1), primary_key=True)
    abbreviate = Column(CHAR(2), nullable=False)
    description = Column(String(40), server_default=text('NULL::character varying'))

    actions = relationship('Action', back_populates='attack_type')


class FaulTypes(Base):
    __tablename__ = 'faul_types'

    id = Column(SmallInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1), primary_key=True)
    abbreviate = Column(CHAR(2), nullable=False)
    description = Column(String(30), server_default=text('NULL::character varying'))

    fauls = relationship('Faul', back_populates='faul_type')


class PlayTypeDict(Base):
    __tablename__ = 'play_type_dict'

    id = Column(SmallInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1), primary_key=True)
    abbreviate = Column(CHAR(3), nullable=False)
    description = Column(String(40), server_default=text('NULL::character varying'))

    throws = relationship('Throw', back_populates='play_type')


class ResultDict(Base):
    __tablename__ = 'result_dict'

    id = Column(SmallInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1), primary_key=True)
    result = Column(CHAR(1), nullable=False)
    res_string = Column(CHAR(15), server_default=text('NULL::bpchar'))


class StartAttackDict(Base):
    __tablename__ = 'start_attack_dict'

    id = Column(SmallInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1), primary_key=True)
    start_attack_type = Column(String(5), nullable=False)
    description = Column(String(40))

    actions = relationship('Action', back_populates='start_attack_type')


class TimeDict(Base):
    __tablename__ = 'time_dict'

    id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    time = Column(String(2), nullable=False)

    actions = relationship('Action', back_populates='time')


class TimeTypeDict(Base):
    __tablename__ = 'time_type_dict'

    id = Column(SmallInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1), primary_key=True)
    time_type = Column(INT4RANGE, nullable=False)

    actions = relationship('Action', back_populates='time_type')
