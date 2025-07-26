from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from expenses.database import Session as SessionLocal
from expenses import schemas, operations

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses/", response_model=schemas.ExpenseOut)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return operations.add_expense(db, expense)

@app.get("/expenses/", response_model=list[schemas.ExpenseOut])
def list_expenses(db: Session = Depends(get_db)):
    return operations.get_expenses(db)
