"""REST-эндпоинты для создания и просмотра коротких ссылок."""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.link_repository import LinkRepository
from app.schemas.link import LinkCreate, LinkResponse
from app.services.shortener import generate_short_code

# Итоговый путь: /api/v1/links (префиксы задаются в router.py)
router = APIRouter(prefix="/links", tags=["Links"])


def build_link_response(request: Request, link) -> LinkResponse:
    """Собирает ответ API: добавляет полный short_url на основе хоста запроса."""
    short_url = str(request.base_url).rstrip("/") + f"/r/{link.short_code}"
    return LinkResponse(
        id=link.id,
        original_url=link.original_url,
        short_code=link.short_code,
        short_url=short_url,
        created_at=link.created_at,
    )


@router.post("", response_model=LinkResponse, status_code=201)
def create_short_link(payload: LinkCreate, request: Request, db: Session = Depends(get_db)):
    """
    Создаёт короткую ссылку.
    Генерирует случайный код; при коллизии повторяет до 10 раз.
    """
    repository = LinkRepository(db)

    tries = 0
    while tries < 10:
        short_code = generate_short_code()
        # Код должен быть уникальным в таблице links
        if repository.get_by_code(short_code) is None:
            link = repository.create(original_url=str(payload.original_url), short_code=short_code)
            return build_link_response(request, link)
        tries += 1

    raise HTTPException(status_code=500, detail="Could not generate a unique short code")


@router.get("", response_model=list[LinkResponse])
def list_links(request: Request, db: Session = Depends(get_db)):
    """Возвращает список всех сокращённых ссылок (новые сверху)."""
    repository = LinkRepository(db)
    links = repository.list_all()
    return [build_link_response(request, link) for link in links]


@router.get("/{short_code}", response_model=LinkResponse)
def get_link(short_code: str, request: Request, db: Session = Depends(get_db)):
    """Возвращает информацию о ссылке по короткому коду (без редиректа)."""
    repository = LinkRepository(db)
    link = repository.get_by_code(short_code)

    if link is None:
        raise HTTPException(status_code=404, detail="Short link not found")

    return build_link_response(request, link)
