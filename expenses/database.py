from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://aleksandrkogalenok@localhost:5432/finance_db"

# echo=True покажет SQL-запросы в консоли, можно выключить
engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(bind=engine,
                             autoflush=False,
                             autocommit=False)

Base = declarative_base()
