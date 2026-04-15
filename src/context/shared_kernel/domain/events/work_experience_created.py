from dataclasses import dataclass

from src.context.shared_kernel.domain.enums import WorkExperienceEventType
from src.context.shared_kernel.domain.events.event_message import EventMessage


@dataclass
class WorkExperienceCreated:
    work_experience_id: str
    profile_id: str
    user_id: str
    company: str
    position: str
    description: str

    def to_event_message(self) -> EventMessage["WorkExperienceCreated"]:
        return EventMessage.create(
            event_type=WorkExperienceEventType.CREATED,
            payload=self,
        )
