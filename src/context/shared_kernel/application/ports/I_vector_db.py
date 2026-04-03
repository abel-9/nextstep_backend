from abc import ABC, abstractmethod
from qdrant_client import AsyncQdrantClient


class IVectorDB(ABC):
    @abstractmethod
    async def connect(self) -> None:
        pass

    @abstractmethod
    def get_client(self) -> AsyncQdrantClient:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass
