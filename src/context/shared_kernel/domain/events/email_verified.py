from dataclasses import dataclass

from src.context.shared_kernel.domain.events.event_message import EventMessage
from src.context.shared_kernel.domain.enums import UserEventType


@dataclass
class EmailVerifiedEvent:
    email: str
    user_id: str

    def to_event_message(self) -> EventMessage["EmailVerifiedEvent"]:
        return EventMessage.create(
            event_type=UserEventType.USER_VERIFIED,
            payload=self,
        )
