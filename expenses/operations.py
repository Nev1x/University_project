from sqlalchemy.orm import Session
from . import models, schemas

def add_expense(db: Session, expense: schemas.ExpenseCreate):
    new_expense = models.Expense(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

def get_expenses(db: Session):
    return db.query(models.Expense).all()
