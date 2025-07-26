from expenses.database import Base, engine
from expenses.models import Expense

Base.metadata.create_all(engine)
