from abc import ABC, abstractmethod
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class IDatabase(ABC):
    @abstractmethod
    async def connect(self) -> None:
        pass

    @abstractmethod
    def get_client(self) -> AsyncIOMotorClient:
        pass

    @abstractmethod
    def get_database(self, database_name: str | None = None) -> AsyncIOMotorDatabase:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass
