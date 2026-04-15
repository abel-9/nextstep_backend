from dataclasses import dataclass
from typing import ClassVar

# metadate
from src.context.chat.domain.value_objects import Metadata

# enums
from src.context.chat.domain.enums import PointKindEnums


@dataclass(frozen=True)
class EducationMetadata(Metadata):
    Kind: ClassVar[str] = PointKindEnums.EDUCATION.value
    education_id: str
    user_id: str
    profile_id: str
    major: str
    description: str

    def to_content(self) -> str:
        return f"Title: {self.major}\nDescription: {self.description}"
