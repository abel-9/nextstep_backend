from pydantic import BaseModel, ConfigDict


class Location(BaseModel):
    country: str
    region: str | None = None
    remote_allowed: bool | None = None

    model_config = ConfigDict(frozen=True)
