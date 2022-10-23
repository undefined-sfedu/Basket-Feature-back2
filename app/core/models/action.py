from sqlalchemy import Integer, Column, ForeignKey, text, SmallInteger, Identity
from sqlalchemy.orm import relationship
from app.core.database import Base


class Action(Base):
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

    active_players = relationship('ActivePlayers')
    attack_type = relationship('AttackTypes')
    possession = relationship('Possessions')
    start_attack_type = relationship('StartAttackDict')
    time = relationship('TimeDict')
    time_type = relationship('TimeTypeDict')

    faul = relationship('Faul')
    loss = relationship('LossDict')
    throw = relationship('Throw')
