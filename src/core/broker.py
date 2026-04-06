from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.core.container import AppContainer

# settings
from src.core.settings import settings

# Addapters
from src.context.shared_kernel.infrastructure.addapters import RabbitMQAdapter


@asynccontextmanager
async def broker_lifespan(container: AppContainer):
    broker = RabbitMQAdapter(
        host=settings.RABBITMQ_HOST,
        exchange_name=settings.RABBITMQ_EXCHANGE_NAME,
        queue_name=settings.QUEUE_NAME,
    )
    await broker.connect()
    container.set_message_broker(broker)
    print("✅ Broker initialized")
    try:
        yield broker
    finally:

        await broker.close()
        print("🛑 Broker closed")
