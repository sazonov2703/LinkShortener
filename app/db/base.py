"""Базовый класс для всех ORM-моделей SQLAlchemy 2.x."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """От него наследуются модели (например Link); metadata используется в create_all."""

    pass
