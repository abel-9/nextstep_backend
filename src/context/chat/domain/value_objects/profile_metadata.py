from dataclasses import dataclass
from typing import ClassVar

from src.context.chat.domain.enums import PointKindEnums
from src.context.chat.domain.value_objects import Metadata


@dataclass
class ProfileMetadata(Metadata):
    kind: ClassVar[str] = PointKindEnums.SCHOLARSHIP.value
    profile_id: str
    user_id: str
    content: str

    def to_content(self) -> str:
        return self.content
