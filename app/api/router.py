"""Сборка всех маршрутов API в один роутер."""

from fastapi import APIRouter

from app.api.routes import links, redirect

# Корневой роутер приложения
api_router = APIRouter()
# CRUD для ссылок: префикс /api/v1 + /links из links.router
api_router.include_router(links.router, prefix="/api/v1")
# Редирект по короткому коду: /r/{short_code}
api_router.include_router(redirect.router)
