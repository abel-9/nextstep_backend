from dataclasses import dataclass
import uuid
from datetime import datetime, timezone


@dataclass
class EventMetadata:
    event_id: str
    event_type: str
    timestamp: str

    @classmethod
    def create(cls, event_type: str) -> "EventMetadata":

        return cls(
            event_id=str(uuid.uuid4()),
            event_type=event_type,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )


@dataclass
class EventMessage[T]:
    metadata: EventMetadata
    payload: T

    @classmethod
    def create(cls, event_type: str, payload: T) -> "EventMessage":
        metadata = EventMetadata.create(event_type)
        return cls(metadata=metadata, payload=payload)

    def dict(self) -> dict:
        return {
            "metadata": {
                "event_id": self.metadata.event_id,
                "event_type": self.metadata.event_type,
                "timestamp": self.metadata.timestamp,
            },
            "payload": self.payload.__dict__,
        }

    @classmethod
    def from_dict(cls, event_message: dict, payload_type: type) -> "EventMessage":
        metadata_dict = event_message.get("metadata", {})
        metadata = EventMetadata(
            event_id=metadata_dict.get("event_id", ""),
            event_type=metadata_dict.get("event_type", ""),
            timestamp=metadata_dict.get("timestamp", ""),
        )
        payload = payload_type(**event_message.get("payload", {}))
        return cls(metadata=metadata, payload=payload)
