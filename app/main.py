"""Точка входа приложения: создание FastAPI и инициализация БД при старте."""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models.link import Link  # noqa: F401 — импорт нужен, чтобы SQLAlchemy зарегистрировала модель

# Экземпляр приложения; title/version берутся из настроек
app = FastAPI(title=settings.app_name, version=settings.app_version)
# Подключаем все маршруты API (links, redirect)
app.include_router(api_router)


@app.on_event("startup")
def on_startup() -> None:
    """При запуске сервера создаём таблицы в БД, если их ещё нет."""
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Health"])
def health_check():
    """Проверка, что сервис запущен (удобно для мониторинга и демо)."""
    return {"status": "ok", "message": "Link Shortener API is running"}
