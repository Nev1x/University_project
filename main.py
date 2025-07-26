from datetime import datetime
from pathlib import Path
import os, pprint

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from expenses.database import SessionLocal
from expenses import operations, schemas

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(title="Expense Tracker")

# ───────────────────────── helpers (debug only) ──────────────────────
def debug_templates():
    sp = templates.env.loader.searchpath[0]          # ← абсолютный путь
    print("SEARCH PATH:", sp)
    print("FILES      :", pprint.pformat(os.listdir(sp)))
    print("HAS index  :", os.path.exists(os.path.join(sp, "index.html")))
# ---------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def read_expenses(request: Request):
    debug_templates()                                # ← выводим один раз
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
