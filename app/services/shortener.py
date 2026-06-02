"""Сервисный слой: генерация коротких кодов для ссылок."""

import random
import string

from app.core.config import settings


def generate_short_code(length: int | None = None) -> str:
    """
    Генерирует случайный короткий код из латинских букв и цифр.
    Длина по умолчанию задаётся в settings.short_code_length.
    """
    code_length = length or settings.short_code_length
    alphabet = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return "".join(random.choices(alphabet, k=code_length))
