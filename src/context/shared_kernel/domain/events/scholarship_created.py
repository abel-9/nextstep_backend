from dataclasses import dataclass
from datetime import date

from src.context.shared_kernel.domain.enums import ScholarshipEventType
from src.context.shared_kernel.domain.events.event_message import EventMessage


@dataclass
class ScholarshipCreated:
    listing_id: str
    title: str
    description: str
    eligibility_summary: str
    provider_name: str
    tags: list[str]
    deadline: str | None

    @classmethod
    def from_primitives(
        cls,
        listing_id: str,
        title: str,
        description: str,
        eligibility_summary: str,
        provider_name: str,
        tags: list[str],
        deadline: date | None,
    ) -> "ScholarshipCreated":
        return cls(
            listing_id=listing_id,
            title=title,
            description=description,
            eligibility_summary=eligibility_summary,
            provider_name=provider_name,
            tags=tags,
            deadline=deadline.isoformat() if deadline else None,
        )

    def to_event_message(self) -> EventMessage["ScholarshipCreated"]:
        return EventMessage.create(
            event_type=ScholarshipEventType.CREATED,
            payload=self,
        )
