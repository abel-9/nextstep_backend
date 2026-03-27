from datetime import datetime, timezone
from typing import Any, Dict
import json
import uuid
import pika

# port definition
from src.context.shared_kernel.application.ports import IMessageBroker

# Type definitions for the message structure
from src.context.shared_kernel.domain.events import EventMessage


class RabbitMQAdapter(IMessageBroker):
    def __init__(
        self, host: str = "localhost", exchange_name: str = "nextstep.events"
    ) -> None:
        self.host: str = host
        self.exchange_name: str = exchange_name

        # Connection parameters with explicit typing
        self.connection = pika.BlockingConnection(
            params=pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

        self.channel.exchange_declare(
            exchange=self.exchange_name, exchange_type="topic", durable=False
        )

    def publish_event(
        self, routing_key: str, event_type: str, payload: Dict[str, Any]
    ) -> None:
        """
        Publishes a strictly typed message to RabbitMQ.
        """
        # Constructing the message using the TypedDict structure
        message: EventMessage = {
            "metadata": {
                "event_id": str(uuid.uuid4()),
                "event_type": event_type,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
            "data": payload,
        }

        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2, content_type="application/json"
            ),
        )

    def close(self) -> None:
        if self.connection.is_open:
            self.connection.close()
