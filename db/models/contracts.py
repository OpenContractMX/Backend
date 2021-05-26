from sqlalchemy import Column, String, Float, DateTime, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Contracts(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    subcontract_id = Column(BigInteger, nullable=False)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    entry_id = Column(String, ForeignKey('comunicacion_transporte._id'), nullable=False)

    # dependency = relationship('Dependencies', back_populates='contracts')
