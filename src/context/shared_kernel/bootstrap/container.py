from functools import lru_cache

from src.core.container import AppContainer

from src.context.shared_kernel.application.ports import (
    ITokenService,
    IEmbedding,
)
from src.context.shared_kernel.infrastructure.addapters import (
    PyJwtService,
    GeminiEmbedding001,
)


class SharedContainer:
    def __init__(self, app_container: AppContainer):
        self.app_container = app_container

    @lru_cache()
    def get_token_service(self) -> ITokenService:
        return PyJwtService()

    @lru_cache()
    def get_embeder(self) -> IEmbedding:
        return GeminiEmbedding001()
