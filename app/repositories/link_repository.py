"""Слой доступа к данным: все SQL-операции с таблицей links."""

from sqlalchemy.orm import Session

from app.models.link import Link


class LinkRepository:
    """Инкапсулирует работу с БД, чтобы маршруты не писали запросы напрямую."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_code(self, short_code: str) -> Link | None:
        """Находит ссылку по короткому коду или возвращает None."""
        return self.db.query(Link).filter(Link.short_code == short_code).first()

    def create(self, original_url: str, short_code: str) -> Link:
        """Сохраняет новую ссылку и возвращает объект с заполненным id."""
        link = Link(original_url=original_url, short_code=short_code)
        self.db.add(link)
        self.db.commit()
        self.db.refresh(link)  # подтянуть id и created_at из БД
        return link

    def list_all(self) -> list[Link]:
        """Все ссылки, сначала последние созданные."""
        return self.db.query(Link).order_by(Link.id.desc()).all()
