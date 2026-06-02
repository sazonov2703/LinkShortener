"""Pydantic-схемы: валидация входящих JSON и формат ответов API."""

from datetime import datetime

from pydantic import BaseModel, HttpUrl


class LinkCreate(BaseModel):
    """Тело запроса POST /api/v1/links."""

    original_url: HttpUrl  # Pydantic проверит, что это валидный URL


class LinkResponse(BaseModel):
    """Ответ API при создании или получении ссылки."""

    id: int
    original_url: str
    short_code: str
    short_url: str  # полный URL для редиректа, собирается в routes/links.py
    created_at: datetime | None

    class Config:
        # Позволяет создавать схему из ORM-объекта Link (атрибуты модели)
        from_attributes = True
