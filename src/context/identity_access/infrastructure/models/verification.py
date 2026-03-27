from datetime import datetime, timezone

from beanie import Document
from pydantic import BeforeValidator, Field
from typing import Annotated


AwareDatetime = Annotated[
    datetime,
    BeforeValidator(
        lambda v: v.replace(tzinfo=timezone.utc) if v.tzinfo is None else v
    ),
]


class Verification(Document):
    id: str = Field(alias="_id")
    identity: str
    type: str
    delivery_method: str
    token: str
    expires_at: AwareDatetime
    is_used: bool = False

    class Settings:
        name = "verifications"
