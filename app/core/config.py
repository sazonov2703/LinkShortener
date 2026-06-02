"""Настройки приложения (имя API, БД, длина короткого кода)."""

from pydantic import BaseModel


class Settings(BaseModel):
    """Значения по умолчанию; при необходимости можно вынести в .env."""

    app_name: str = "Link Shortener API"
    app_version: str = "1.0.0"
    database_url: str = "sqlite:///./link_shortener.db"  # файл БД в корне проекта
    short_code_length: int = 6  # длина случайного кода (буквы + цифры)


settings = Settings()
