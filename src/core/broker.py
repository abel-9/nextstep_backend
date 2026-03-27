from functools import lru_cache

# massahge broker interface
from src.context.shared_kernel.application.ports import IMessageBroker

# RabitMQ Addapter
from src.context.shared_kernel.infrastructure.addapters import RabbitMQAdapter

# Settings for the message broker
from src.core.settings import settings


@lru_cache
def get_message_broker() -> IMessageBroker:
    return RabbitMQAdapter(
        host=settings.RABBITMQ_HOST, exchange_name=settings.RABBITMQ_EXCHANGE_NAME
    )
