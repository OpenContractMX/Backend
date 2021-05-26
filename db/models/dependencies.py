from sqlalchemy import Column, String, Float, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Dependencies(Base):

    __tablename__ = 'comunicacion_transporte'

    # def __init__(self, table):
    #     self.__tablename__ = table

    id = Column(Integer, primary_key=True)
    _id = Column(String)
    buyer_id = Column(String, nullable=False)
    buyer_name = Column(String, nullable=False)
    cycle = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    expedition_day = Column(Float, nullable=False)
    expedition_month = Column(Float, nullable=False)
    expedition_trimester = Column(Float, nullable=False)
    expedition_year = Column(Float, nullable=False)
    tag = Column(String, nullable=False)

    # contracts = relationship('Contracts', back_populates='dependency', foreign_keys=['entry_id'])