from pydantic import BaseModel
from fastapi import APIRouter, Depends
from backend.database import get_db
from backend.models import Holding
from sqlalchemy.orm import Session

class HoldingCreate(BaseModel):
    ticker: str
    shares: float
    avg_cost_basis: float

router = APIRouter()

@router.get("/holdings")
def get_holdings(db: Session = Depends(get_db)):
    return db.query(Holding).all()

@router.post("/holdings")
def create_holding(holding: HoldingCreate, db: Session = Depends(get_db)):
    db_holding = Holding(
        ticker=holding.ticker,
        shares=holding.shares,
        avg_cost_basis=holding.avg_cost_basis
    )
    db.add(db_holding)
    db.commit()
    db.refresh(db_holding)
    return db_holding

@router.put("/holdings/{id}")
def update_holding(id: int, holding: HoldingCreate, db: Session = Depends(get_db)):
    db_holding = db.query(Holding).filter(Holding.id == id).first()
    if not db_holding:
        return {"error": "Holding not found"}
    db_holding.ticker = holding.ticker
    db_holding.shares = holding.shares
    db_holding.avg_cost_basis = holding.avg_cost_basis
    db.commit()
    db.refresh(db_holding)
    return db_holding

@router.delete("/holdings/{id}")
def delete_holding(id: int, db: Session = Depends(get_db)):
    db_holding = db.query(Holding).filter(Holding.id == id).first()
    if not db_holding:
        return {"error": "Holding not found"}
    db.delete(db_holding)
    db.commit()
    return {"message": "Holding deleted"}