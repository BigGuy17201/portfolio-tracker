from backend.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

class Holding(Base):
    __tablename__ = "holdings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ticker = Column(String)
    shares = Column(Float)
    avg_cost_basis = Column(Float)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ticker = Column(String)
    type = Column(String)
    shares = Column(Float)
    price = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)