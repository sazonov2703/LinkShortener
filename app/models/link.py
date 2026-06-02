"""ORM-модель таблицы links в базе данных."""

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Link(Base):
    """Одна запись = одна сокращённая ссылка."""

    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    original_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    # unique + index: быстрый поиск по коду и защита от дубликатов
    short_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
