from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Link Shortener API"
    app_version: str = "1.0.0"
    database_url: str = "sqlite:///./link_shortener.db"
    short_code_length: int = 6


settings = Settings()
