from abc import ABC, abstractmethod

# Domain Aggregate
from src.context.chat.domain.entities import ProfileAggregate


class IProfileDocumentRepository:
    @abstractmethod
    def save(self, education: ProfileAggregate) -> None:
        pass

    @abstractmethod
    def update(self, education: ProfileAggregate) -> None:
        pass
