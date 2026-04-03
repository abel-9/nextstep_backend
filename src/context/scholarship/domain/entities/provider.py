from src.context.scholarship.domain.value_object.provider_id import ProviderId
from src.context.scholarship.domain.value_object.url import Url
from pydantic import BaseModel, ConfigDict


class Provider(BaseModel):
    id: ProviderId
    name: str
    website: Url
    country: str
    verified: bool

    model_config = ConfigDict(frozen=True)
