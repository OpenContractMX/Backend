from sqlalchemy import Column, String, Float, DateTime, BigInteger, Integer, ForeignKey
from db.session import Base

class ComunicacionTransporte(Base):
    table_name = ""

    #def __init__(self,table):
    #    ComunicacionTransporte.table_name += table


    __tablename__ = "comunicacion_transporte"

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

class Contracts(Base):

    dependency_name = ""

    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True)
    subcontract_id = Column(BigInteger, nullable=False)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    entry_id = Column(String, ForeignKey('comunicacion_transporte._id'), nullable=False)
