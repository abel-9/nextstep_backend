from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.context.shared_kernel.application.ports import IMotorDB


class MotorDBAdapter(IMotorDB):
    def __init__(self, url: str, default_db_name: str):
        self.url = url
        self.default_db_name = default_db_name
        self._client: AsyncIOMotorClient | None = None

    async def connect(self) -> None:
        self._client = AsyncIOMotorClient(self.url)

    def get_client(self) -> AsyncIOMotorClient:
        if self._client is None:
            raise RuntimeError("MotorDBAdapter not connected. Call connect() first.")
        return self._client

    def get_database(self, database_name: str | None = None) -> AsyncIOMotorDatabase:
        client = self.get_client()
        return client[database_name or self.default_db_name]

    async def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None
