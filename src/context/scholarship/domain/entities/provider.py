from src.context.scholarship.domain.value_object.url import Url
from pydantic import BaseModel, ConfigDict


class Provider(BaseModel):
    name: str
    website: Url
    country: str
    verified: bool

    model_config = ConfigDict(frozen=True)
