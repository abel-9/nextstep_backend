import json
import aio_pika
from typing import Callable

# Assuming these are your existing port/type definitions
from src.context.shared_kernel.application.ports import IMessageBroker
from src.context.shared_kernel.domain.events.event_message import EventMessage


class RabbitMQAdapter(IMessageBroker):
    def __init__(self, host: str, exchange_name: str | None, queue_name: str) -> None:
        self.host = host
        self.exchange_name = exchange_name or ""
        self.queue_name = queue_name
        self.connection: aio_pika.RobustConnection | None = None
        self.channel: aio_pika.RobustChannel | None = None

    async def connect(self):
        # connect_robust handles automatic reconnects for you
        self.connection = await aio_pika.connect_robust(f"amqp://{self.host}/")
        self.channel = await self.connection.channel()

    async def consume(self, event_type: str, callback: Callable):
        # Ensure the queue exists
        queue = await self.channel.declare_queue(event_type, durable=False)

        # Define a wrapper to handle the message processing
        async def on_message(message: aio_pika.IncomingMessage):
            async with message.process():
                # Pass the body (parsed) to your domain callback
                await callback(json.loads(message.body.decode()))

        await queue.consume(on_message)
        print(f" [*] Waiting for messages on {event_type}. To exit press CTRL+C")

    async def publish(self, event_type: str, event_message: EventMessage) -> None:
        if not self.channel:
            raise RuntimeError("Adapter not connected. Call connect() first.")

        # Declare queue before publishing (matching your original logic)
        await self.channel.declare_queue(event_type, durable=False)

        await self.channel.default_exchange.publish(
            aio_pika.Message(
                body=json.dumps(event_message.dict()).encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            ),
            routing_key=event_type,
        )

    async def close(self) -> None:
        if self.connection and not self.connection.is_closed:
            await self.connection.close()
