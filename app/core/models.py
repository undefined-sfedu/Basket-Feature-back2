from sqlalchemy import ARRAY, Boolean, CHAR, Column, DateTime, ForeignKey, Identity, Integer, SmallInteger, String, text
from sqlalchemy.dialects.postgresql import INT4RANGE
from sqlalchemy.orm import relationship
from app.core.database import Base


class AttackTypes(Base):
    __tablename__ = 'attack_types'

    id = Column(SmallInteger,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1),
                primary_key=True)
    abbreviate = Column(CHAR(2), nullable=False)
    description = Column(String(40), server_default=text('NULL::character varying'))


class FaulTypes(Base):
    __tablename__ = 'faul_types'

    id = Column(SmallInteger,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1),
                primary_key=True)
    abbreviate = Column(CHAR(2), nullable=False)
    description = Column(String(30), server_default=text('NULL::character varying'))


class LossDict(Base):
    __tablename__ = 'loss_dict'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    abbreviate = Column(CHAR(3), nullable=False)
    description = Column(String(30), server_default=text('NULL::character varying'))


class PlayTypeDict(Base):
    __tablename__ = 'play_type_dict'

    id = Column(SmallInteger,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1),
                primary_key=True)
    abbreviate = Column(CHAR(3), nullable=False)
    description = Column(String(40), server_default=text('NULL::character varying'))


class Possessions(Base):
    __tablename__ = 'possessions'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    players_array = Column(ARRAY(Integer()), nullable=False)


class ResultDict(Base):
    __tablename__ = 'result_dict'

    id = Column(SmallInteger,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1),
                primary_key=True)
    abbreviate = Column(CHAR(1), nullable=False)
    description = Column(CHAR(15), server_default=text('NULL::bpchar'))


class StartAttackDict(Base):
    __tablename__ = 'start_attack_dict'

    id = Column(SmallInteger,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1),
                primary_key=True)
    abbreviate = Column(String(5), nullable=False)
    description = Column(String(40))


class TimeDict(Base):
    __tablename__ = 'time_dict'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    time = Column(String(2), nullable=False)


class TimeTypeDict(Base):
    __tablename__ = 'time_type_dict'

    id = Column(SmallInteger,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=32767, cycle=False, cache=1),
                primary_key=True)
    time_type = Column(INT4RANGE, nullable=False)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    email = Column(String(64), nullable=False)
    pass_hash = Column(CHAR(64), nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    middle_name = Column(String(30))

    teams = relationship('Teams', back_populates='user')
    games = relationship('Games', back_populates='user')


class Fauls(Base):
    __tablename__ = 'fauls'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    faul_type_id = Column(ForeignKey('faul_types.id'), nullable=False)
    scored = Column(SmallInteger, nullable=False, server_default=text('0'))

    faul_type = relationship('FaulTypes')


class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    name = Column(String(100), nullable=False)
    user_id = Column(ForeignKey('users.id'))

    user = relationship('Users', back_populates='teams')
    players = relationship('Players', back_populates='team')


class Throws(Base):
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


class Players(Base):
    __tablename__ = 'players'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    number = Column(SmallInteger, nullable=False, server_default=text('1'))
    team_id = Column(ForeignKey('teams.id'), nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    middle_name = Column(String(30))

    team = relationship('Teams', back_populates='players')


class ActivePlayers(Base):
    __tablename__ = 'active_players'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    first_player_id = Column(ForeignKey('players.id'), nullable=False)
    second_player_id = Column(ForeignKey('players.id'), nullable=False)
    third_player_id = Column(ForeignKey('players.id'), nullable=False)
    fourth_player_id = Column(ForeignKey('players.id'), nullable=False)
    fifth_player_id = Column(ForeignKey('players.id'), nullable=False)

    fifth_player = relationship('Players', foreign_keys=[fifth_player_id])
    first_player = relationship('Players', foreign_keys=[first_player_id])
    fourth_player = relationship('Players', foreign_keys=[fourth_player_id])
    second_player = relationship('Players', foreign_keys=[second_player_id])
    third_player = relationship('Players', foreign_keys=[third_player_id])


class Actions(Base):
    __tablename__ = 'actions'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    time_type_id = Column(ForeignKey('time_type_dict.id'), nullable=False, server_default=text('1'))
    seconds = Column(SmallInteger, nullable=False)
    possession_id = Column(ForeignKey('possessions.id'), nullable=False)
    active_players_id = Column(ForeignKey('active_players.id'), nullable=False)
    time_id = Column(ForeignKey('time_dict.id'), nullable=False)
    start_attack_type_id = Column(ForeignKey('start_attack_dict.id'), nullable=False)
    attack_type_id = Column(ForeignKey('attack_types.id'), nullable=False)
    throw_id = Column(ForeignKey('throws.id'))
    loss_id = Column(ForeignKey('loss_dict.id'))
    faul_id = Column(ForeignKey('fauls.id'))
    game_id = Column(ForeignKey('games.id'))

    active_players = relationship('ActivePlayers')
    attack_type = relationship('AttackTypes')
    faul = relationship('Fauls')
    loss = relationship('LossDict')
    possession = relationship('Possessions')
    start_attack_type = relationship('StartAttackDict')
    throw = relationship('Throws')
    time = relationship('TimeDict')
    time_type = relationship('TimeTypeDict')


class Games(Base):
    __tablename__ = 'games'

    id = Column(Integer,
                Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
                primary_key=True)
    team_a_id = Column(ForeignKey('teams.id'), nullable=False)
    team_b_id = Column(ForeignKey('teams.id'), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    start_five_id = Column(ForeignKey('active_players.id'), nullable=False)
    date = Column(DateTime)

    start_five = relationship('ActivePlayers')
    team_a = relationship('Teams', foreign_keys=[team_a_id])
    team_b = relationship('Teams', foreign_keys=[team_b_id])
    user = relationship('Users', back_populates='games')
    actions = relationship('Actions')
