# Expense Tracker

Простое веб-приложение на **FastAPI** для учёта личных расходов с хранением данных в PostgreSQL и минималистичным интерфейсом на Jinja2 + HTML/CSS.

---

## Содержание
1. [Описание](#описание)  
2. [Стек технологий](#стек-технологий)
3. [Развёртывание](#развёртывание)  
4. [Инициализация базы](#инициализация-базы)  
5. [Точки маршрутов / API](#точки-маршрутов--api)  
6. [Модели данных](#модели-данных)  
7. [Примеры работы](#примеры-работы)  

---

## Описание

Приложение позволяет:  
* добавлять расход с категорией, суммой и описанием;  
* просматривать список расходов в обратном хронологическом порядке.

Это учебный проект, выполненный в рамках производственной практики для демонстрации навыков работы с **FastAPI**, **SQLAlchemy** и системой шаблонов **Jinja2**.

## Стек технологий

| Слой            | Технологии |
|-----------------|------------|
| Backend         | Python 3.12, [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy 2.x](https://docs.sqlalchemy.org/) |
| База данных     | PostgreSQL 15 |
| Frontend (view) | Jinja2 templates, чистый HTML 5, CSS 3 (шрифт [Inter](https://rsms.me/inter)) |
| Dev‐инструменты | `pip`, `virtualenv`, `uvicorn`, `psql`, `pytest` (пока не настроен) |

## Развёртывание

> Шаги для локального запуска под Linux/macOS; в Windows команды аналогичны (PowerShell).

```bash
# 1. Клонируем репозиторий
git clone https://github.com/<username>/expense-tracker.git
cd expense-tracker

# 2. Создаём и активируем виртуальное окружение
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Экспортируем переменную подключения к БД (или изменяем в expenses/database.py)
export DATABASE_URL="postgresql://user:password@localhost:5432/finance_db"

# 5. Создаём таблицы
python init_db.py

# 6. Запускаем сервер разработки
uvicorn main:app --reload
# Откройте http://127.0.0.1:8000 в браузере
```

## Инициализация базы

Если структура БД ещё не создана — запустите скрипт **init_db.py**, который импортирует Base и вызывает Base.metadata.create_all(engine).
Для production-миграций рекомендуется Alembic.

## Точки маршрутов / API

| Метод | URL   | Шаблон / действие                 | Описание                                   |
|-------|-------|-----------------------------------|--------------------------------------------|
| `GET` | `/`   | `index.html` → `read_expenses`    | Список всех расходов                       |
| `GET` | `/add`| `add_expense.html` → `add_expense_form` | Форма создания расхода                     |
| `POST`| `/add`| `add_expense`                     | Обработка формы и сохранение записи в БД   |

## Модели данных

```bash
class Expense(Base):
    id: int                 # PK
    category: str
    amount: float
    description: str | None
    date: datetime          # server_default=func.now()
```

## Примеры работы

* Добавление: заполняем форму /add; сервер выполняет operations.create_expense, после чего делает редирект 303 на главную страницу.
* Просмотр: на главной Jinja2 выводит список {% for exp in expenses %} с форматированием даты и суммы.
