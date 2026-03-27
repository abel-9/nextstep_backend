from typing import TypedDict, Any, Dict


class EventMetadata(TypedDict):
    event_id: str
    event_type: str
    timestamp: str


class EventMessage(TypedDict):
    metadata: EventMetadata
    data: Dict[str, Any]
