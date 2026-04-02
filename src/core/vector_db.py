from contextlib import asynccontextmanager
from qdrant_client import AsyncQdrantClient


@asynccontextmanager
async def vector_db_lifespan():
    qdrant_client = AsyncQdrantClient(
        url="http://localhost:6333",
    )
    print("✅ Vector DB (Qdrant) initialized")
    try:
        yield qdrant_client
    finally:
        await qdrant_client.close()
        print("🛑 Vector DB (Qdrant) closed")
