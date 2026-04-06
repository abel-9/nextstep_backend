from typing import Any
from mediator.event import LocalEventBus
from mediator.request import LocalRequestBus
from src.core.interfaces import IMediator


class PythonMediatorAdapter(IMediator):
    def __init__(self, event_bus: LocalEventBus, request_bus: LocalRequestBus):
        self.__event_bus = event_bus
        self.__request_bus = request_bus

    async def publish(self, event: Any) -> None:
        # Map our internal Port call to the library's method
        await self.__event_bus.publish(event)

    async def send(self, request: Any) -> Any:
        # Map our internal Port call to the library's method
        return await self.__request_bus.execute(request)

    def get_event_bus(self) -> LocalEventBus:
        return self.__event_bus

    def get_request_bus(self) -> LocalRequestBus:
        return self.__request_bus
