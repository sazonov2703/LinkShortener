from sqlalchemy.orm import Session

from app.models.link import Link


class LinkRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_code(self, short_code: str) -> Link | None:
        return self.db.query(Link).filter(Link.short_code == short_code).first()

    def create(self, original_url: str, short_code: str) -> Link:
        link = Link(original_url=original_url, short_code=short_code)
        self.db.add(link)
        self.db.commit()
        self.db.refresh(link)
        return link

    def list_all(self) -> list[Link]:
        return self.db.query(Link).order_by(Link.id.desc()).all()
