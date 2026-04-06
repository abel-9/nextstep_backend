from contextlib import asynccontextmanager

from mediator.event import LocalEventBus
from mediator.request import LocalRequestBus

# Core Container
from src.core.container import AppContainer

# the interface for the bus
from src.context.shared_kernel.application.ports import IMediator

# the adapter for the event bus
from src.core.adapters import PythonMediatorAdapter


@asynccontextmanager
async def mediator_lifespan(container: AppContainer):
    event_bus = LocalEventBus()
    request_bus = LocalRequestBus()
    mediator = PythonMediatorAdapter(event_bus=event_bus, request_bus=request_bus)
    container.set_mediator(mediator)
    print("✅ Mediator initialized")
    try:
        yield mediator
    finally:
        print("🛑 Mediator closed")
