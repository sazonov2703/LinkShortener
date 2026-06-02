"""Базовый класс для всех ORM-моделей SQLAlchemy 2.x."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
