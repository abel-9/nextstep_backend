from dataclasses import dataclass
from typing import ClassVar

from src.context.chat.domain.enums import PointKindEnums
from src.context.chat.domain.value_objects import Metadata


@dataclass(frozen=True)
class WorkExperienceMetadata(Metadata):
    Kind: ClassVar[str] = PointKindEnums.WORK_EXPERIENCE.value
    work_experience_id: str
    user_id: str
    profile_id: str
    company: str
    position: str
    description: str

    def to_content(self) -> str:
        return (
            f"Company: {self.company}\n"
            f"Position: {self.position}\n"
            f"Description: {self.description}"
        )
