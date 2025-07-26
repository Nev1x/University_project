from expenses.database import Base, engine
from expenses.models import Expense  # noqa: F401  (нужен для регистрации модели)

print("Создаем таблицы...")
Base.metadata.create_all(engine)
print("Готово.")
