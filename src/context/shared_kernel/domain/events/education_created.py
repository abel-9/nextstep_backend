from dataclasses import dataclass
from datetime import datetime

# Event Message
from src.context.shared_kernel.domain.events.event_message import EventMessage

# Event type
from src.context.shared_kernel.domain.enums import EducationEventType


@dataclass
class EducationCreated:
    education_id: str
    profile_id: str
    user_id: str
    major: str
    description: str

    def to_event_message(self) -> EventMessage["EducationCreated"]:
        return EventMessage.create(
            event_type=EducationEventType.CREATED,
            payload=self,
        )
