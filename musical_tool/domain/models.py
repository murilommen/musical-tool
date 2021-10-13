from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from musical_tool.infrastructure.context_manager import Base


class Analysis(Base):
    __tablename__ = 'analysis'

    id = Column('id', Integer, primary_key=True, index=True)
    user_name = Column('user_name', String)
    user_group = Column('user_group', String)
    param_low = Column('param_low', String)
    param_high = Column('param_high', String)
    id_music = Column('music_id', ForeignKey('music.id'), Integer)

    time = relationship('Time')


class Music(Base):
    __tablename__ = 'music'

    id = Column('id', Integer, primary_key=True, index=True)
    music_name = Column('music_name', String)

    analysis = relationship('Analysis')


class Time(Base):
    __tablename__ = 'time'

    id = Column('id', Integer, primary_key=True, index=True)
    id_analysis = Column('id_analysis', ForeignKey('analysis.id'), Integer)
    timestamp = Column('timestamp', Integer)
    value = Column('value', Float)
