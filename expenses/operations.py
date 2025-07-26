from sqlalchemy.orm import Session
from . import models, schemas

def create_expense(db: Session, data: schemas.ExpenseCreate):
    obj = models.Expense(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def list_expenses(db: Session):
    return db.query(models.Expense).order_by(models.Expense.date.desc()).all()
