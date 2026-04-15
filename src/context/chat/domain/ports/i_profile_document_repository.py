from abc import ABC, abstractmethod

# Domain Aggregate
from src.context.chat.domain.entities import ProfileAggregate


class IProfileDocumentRepository(ABC):
    @abstractmethod
    async def get_by_profile_id(
        self, profile_id: str, user_id: str
    ) -> ProfileAggregate | None:
        pass

    @abstractmethod
    async def save(self, profile_aggregate: ProfileAggregate) -> None:
        pass

    @abstractmethod
    async def update(self, profile_aggregate: ProfileAggregate) -> None:
        pass
