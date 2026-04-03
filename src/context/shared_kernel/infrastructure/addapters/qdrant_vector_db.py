from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.http.exceptions import UnexpectedResponse

# Interface
from src.context.shared_kernel.application.ports import IVectorDB


class QdrantVectorDBAdapter(IVectorDB):
    def __init__(self, url: str, collection_name: str, vector_size: int):
        self._client = None
        self.collection_name = collection_name
        self.vector_size = vector_size
        self.url = url

    async def connect(self) -> None:
        """
        Initializes an in-memory Qdrant client.
        Data is lost when the process ends—perfect for testing.
        """
        self._client = AsyncQdrantClient(url=self.url)

        # Pre-create a collection so the fake is ready to use
        exists = await self._client.get_collection(collection_name=self.collection_name)
        if not exists:
            await self._client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size, distance=Distance.COSINE
                ),
            )

    def get_client(self) -> AsyncQdrantClient:
        if not self._client:
            raise RuntimeError("FakeVectorDB not connected. Call connect() first.")
        return self._client

    async def close(self) -> None:
        if self._client:
            await self._client.close()
            print("Qdrant connection closed")
