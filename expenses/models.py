from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String)
    date = Column(DateTime, server_default=func.now())
