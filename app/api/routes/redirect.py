from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.link_repository import LinkRepository

router = APIRouter(prefix="/r", tags=["Redirect"])


@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    repository = LinkRepository(db)
    link = repository.get_by_code(short_code)

    if link is None:
        raise HTTPException(status_code=404, detail="Short link not found")

    return RedirectResponse(url=link.original_url, status_code=307)
