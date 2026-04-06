from dataclasses import dataclass

# metadate
from src.context.chat.domain.value_objects import Metadata


@dataclass(frozen=True)
class EducationMetadata(Metadata):
    education_id: str
    user_id: str
    profile_id: str
    major: str
    description: str

    def to_content(self) -> str:
        return f"Title: {self.major}\nDescription: {self.description}"
