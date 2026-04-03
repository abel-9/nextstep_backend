from abc import ABC, abstractmethod


class IDocumentVectorRepository(ABC):
    @abstractmethod
    async def add_vector(self, document_id: str, vector: list[float]) -> None:
        pass

    @abstractmethod
    async def get_vector(self, document_id: str) -> list[float] | None:
        pass

    @abstractmethod
    async def delete_vector(self, document_id: str) -> None:
        pass
