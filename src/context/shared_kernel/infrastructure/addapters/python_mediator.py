from mediator.event import LocalEventBus
from mediator.request import LocalRequestBus
from src.context.shared_kernel.application.ports import IMediator
from typing import Any


class PythonMediator(IMediator):
    def __init__(self, event_bus: LocalEventBus, request_bus: LocalRequestBus):
        self.__event_bus = event_bus
        self.__request_bus = request_bus

    async def publish(self, event: Any) -> None:
        # Map our internal Port call to the library's method
        await self.__event_bus.publish(event)

    async def send(self, request: Any) -> Any:
        # Map our internal Port call to the library's method
        return await self.__request_bus.execute(request)
