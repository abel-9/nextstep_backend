from functools import lru_cache

# ports
from src.context.shared_kernel.application.ports import ITokenService

# Adapters
from src.context.shared_kernel.infrastructure.addapters import PyJwtService


@lru_cache
def get_token_service() -> ITokenService:
    return PyJwtService()
