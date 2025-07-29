from datetime import datetime
from pathlib import Path
import os, pprint

from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from expenses.database import SessionLocal
from expenses import operations, schemas

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(title="Expense Tracker")

# ── подключаем статику ────────────────────────────────────────────
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_expenses(request: Request):
    with SessionLocal() as db:
        expenses = operations.list_expenses(db)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "expenses": expenses}
    )

@app.get("/add", response_class=HTMLResponse)
def add_expense_form(request: Request):
    return templates.TemplateResponse("add_expense.html", {"request": request})

@app.post("/add")
def add_expense(category: str = Form(...),
                amount: float = Form(...),
                description: str = Form(None)):
    with SessionLocal() as db:
        data = schemas.ExpenseCreate(category=category,
                                     amount=amount,
                                     description=description)
        operations.create_expense(db, data)
    return RedirectResponse("/", status_code=303)

