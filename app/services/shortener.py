import random
import string

from app.core.config import settings


def generate_short_code(length: int | None = None) -> str:
    code_length = length or settings.short_code_length
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choices(alphabet, k=code_length))
