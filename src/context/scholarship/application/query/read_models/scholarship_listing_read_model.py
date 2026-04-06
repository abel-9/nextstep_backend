from datetime import date

from pydantic import BaseModel, Field


class ProviderReadModel(BaseModel):
    name: str
    website: str
    country: str
    verified: bool


class MoneyReadModel(BaseModel):
    amount: float
    currency: str


class LocationReadModel(BaseModel):
    country: str
    region: str | None = None
    remote_allowed: bool | None = None


class SourceReadModel(BaseModel):
    type: str
    origin: str
    last_fetched_at: date


class ScholarshipListingReadModel(BaseModel):
    id: str = Field(validation_alias="_id")
    title: str
    description: str
    provider: ProviderReadModel
    external_url: str
    amount: MoneyReadModel | None = None
    deadline: date | None = None
    eligibility_summary: str
    tags: list[str]
    location: LocationReadModel
    status: str
    source: SourceReadModel
    created_at: date
    updated_at: date
