from functools import lru_cache

# ports
from src.context.shared_kernel.application.ports import (
    ITokenService,
    IEmbedding,
    IMessageBroker,
    IMediator,
    IDocumentVectorRepository,
)

# Core
from src.context.shared_kernel.application.ports.I_vector_db import IVectorDB


# Adapters
from src.context.shared_kernel.infrastructure.addapters import (
    PyJwtService,
    GeminiEmbedding001,
    FakeEmbedding,
    PythonMediator,
    RabbitMQAdapter,
    DocumentVectorRepository,
)


@lru_cache
def get_token_service() -> ITokenService:
    return PyJwtService()


@lru_cache
def get_embeder() -> IEmbedding:
    return GeminiEmbedding001()


@lru_cache
def get_mediator() -> IMediator:
    return PythonMediator()


@lru_cache
def get_message_broker() -> IMessageBroker:
    return RabbitMQAdapter()


@lru_cache
def get_document_vector_repository(vector_db: IVectorDB) -> IDocumentVectorRepository:
    return DocumentVectorRepository(vector_db=vector_db)
