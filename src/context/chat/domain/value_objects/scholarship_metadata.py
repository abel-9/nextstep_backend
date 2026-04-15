from dataclasses import dataclass
from typing import ClassVar

from src.context.chat.domain.enums import PointKindEnums
from src.context.chat.domain.value_objects import Metadata


@dataclass(frozen=True)
class ScholarshipMetadata(Metadata):
    Kind: ClassVar[str] = PointKindEnums.SCHOLARSHIP.value
    listing_id: str
    title: str
    description: str
    eligibility_summary: str
    provider_name: str
    tags: list[str]
    deadline: str | None

    def to_content(self) -> str:
        tags = ", ".join(self.tags)
        deadline = self.deadline or "N/A"
        return (
            f"Title: {self.title}\n"
            f"Provider: {self.provider_name}\n"
            f"Deadline: {deadline}\n"
            f"Eligibility: {self.eligibility_summary}\n"
            f"Tags: {tags}\n"
            f"Description: {self.description}"
        )
