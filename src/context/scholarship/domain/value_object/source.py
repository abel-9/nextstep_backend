from datetime import date

from pydantic import BaseModel, ConfigDict

from src.context.scholarship.domain.enums import SourceType


class Source(BaseModel):
    type: SourceType
    origin: str
    last_fetched_at: date

    model_config = ConfigDict(frozen=True)
