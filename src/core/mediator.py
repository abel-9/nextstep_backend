from mediator.event import LocalEventBus
from mediator.request import LocalRequestBus
from functools import lru_cache

# the interface for the bus
from src.context.shared_kernel.application.ports import IMediator

# the adapter for the event bus
from src.context.shared_kernel.infrastructure.addapters import PythonMediator

event_bus = LocalEventBus()
request_bus = LocalRequestBus()


@lru_cache()
def get_mediator() -> IMediator:
    return PythonMediator(event_bus=event_bus, request_bus=request_bus)
