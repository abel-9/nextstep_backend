from typing import Any
from abc import ABC, abstractmethod

from mediator.event import LocalEventBus
from mediator.request import LocalRequestBus


class IMediator(ABC):
    @abstractmethod
    async def publish(self, event: Any) -> None:
        """Publishes an event to all registered subscribers."""
        ...
        pass

    @abstractmethod
    async def send(self, request: Any) -> Any:
        """Sends a request and waits for a response from the appropriate handler."""
        ...
        pass

    def get_event_bus(self) -> LocalEventBus:
        pass

    def get_request_bus(self) -> LocalRequestBus:
        pass
