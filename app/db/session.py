"""Подключение к БД и выдача сессии на каждый HTTP-запрос."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# SQLite по умолчанию запрещает доступ из другого потока;
# для Uvicorn/FastAPI это нужно отключить
connect_args = {}
if settings.database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db() -> Session:
    """
    Dependency FastAPI: открывает сессию на время обработки запроса
    и гарантированно закрывает её в finally.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
