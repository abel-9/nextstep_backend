from typing import Dict, Any
from dataclasses import dataclass
from datetime import datetime, timezone
import uuid


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
class EventMessage:
    metadata: EventMetadata
    data: Dict[str, Any]

    @classmethod
    def create(cls, event_type: str, payload: Dict[str, Any]) -> "EventMessage":
        metadata = EventMetadata.create(event_type)
        return cls(metadata=metadata, data=payload)

    def dict(self) -> Dict[str, Any]:
        return {
            "metadata": {
                "event_id": self.metadata.event_id,
                "event_type": self.metadata.event_type,
                "timestamp": self.metadata.timestamp,
            },
            "data": self.data,
        }
