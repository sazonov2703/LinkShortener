from fastapi import APIRouter

from app.api.routes import links, redirect

api_router = APIRouter()
api_router.include_router(links.router, prefix="/api/v1")
api_router.include_router(redirect.router)
