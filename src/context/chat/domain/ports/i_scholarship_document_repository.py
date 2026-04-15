from abc import ABC, abstractmethod

from src.context.chat.domain.entities import ScholarshipAggregate


class IScholarshipDocumentRepository(ABC):
    @abstractmethod
    async def get_by_listing_id(self, listing_id: str) -> ScholarshipAggregate | None:
        pass

    @abstractmethod
    async def save(self, scholarship_aggregate: ScholarshipAggregate) -> None:
        pass

    @abstractmethod
    async def update(self, scholarship_aggregate: ScholarshipAggregate) -> None:
        pass
