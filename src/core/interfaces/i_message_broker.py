from abc import ABC, abstractmethod

# Base Models
from src.context.shared_kernel.domain.events import EventMessage

# from collections.abc import Callable


class IMessageBroker(ABC):
    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def publish(self, event_type: str, event_message: EventMessage) -> None:
        pass

    @abstractmethod
    async def consume(self, event_type: str, callback):
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

    # @abstractmethod
    # def subscribe(self, topic: str, callback: Callable[[dict], None]) -> None:
    #     pass
