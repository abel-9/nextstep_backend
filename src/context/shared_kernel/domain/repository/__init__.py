from abc import ABC, abstractmethod

# Querys
from src.context.identity_access.application.query.queries import GetUsersQuery


class Repository[T](ABC):
    @abstractmethod
    async def get_all(self, query: GetUsersQuery) -> list[T]:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> T:
        pass

    @abstractmethod
    async def save(self, entity: T) -> None:
        pass

    @abstractmethod
    async def update(self, entity: T) -> None:
        pass

    @abstractmethod
    async def remove(self, entity: T) -> None:
        pass
