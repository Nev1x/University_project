from expenses.database import Base, engine
from expenses.models import Expense

print("Создание таблиц...")
Base.metadata.create_all(engine)
print("Готово.")
