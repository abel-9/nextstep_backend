from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.core.settings import settings
from src.context.shared_kernel.infrastructure.addapters import QdrantVectorDBAdapter


@asynccontextmanager
async def vector_db_lifespan(app: FastAPI):
    vector_db = QdrantVectorDBAdapter(
        url=settings.QDRANT_URL,
        collection_name=settings.COLLECTION_NAME,
        vector_size=settings.VECTOR_SIZE,
    )
    await vector_db.connect()
    app.state.vector_db = vector_db
    print("✅ Vector DB (Qdrant) initialized")
    try:
        yield vector_db
    finally:
        await vector_db.close()
        print("🛑 Vector DB (Qdrant) closed")
