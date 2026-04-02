from pydantic import BaseModel
from fastapi import APIRouter, Depends
from backend.database import get_db
from backend.models import Transaction
from sqlalchemy.orm import Session
from datetime import datetime

class TransactionCreate(BaseModel):
    ticker: str
    type: str
    shares: float
    price: float
    date: datetime

router = APIRouter()

@router.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()

@router.post("/transactions")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = transaction(
        ticker = transaction.ticker,
        type = transaction.type,
        shares = transaction.shares,
        price = transaction.price,
        date = transaction.date
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

#add the rest of the functions from holdings