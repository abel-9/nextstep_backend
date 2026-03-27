from typing import Any
from abc import ABC, abstractmethod


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
