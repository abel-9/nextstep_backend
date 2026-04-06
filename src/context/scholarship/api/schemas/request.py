from datetime import date

from pydantic import BaseModel

from src.context.scholarship.domain.enums import SourceType


class Money(BaseModel):
    amount: float
    currency: str


class Provider(BaseModel):
    name: str
    website: str
    country: str
    verified: bool


class Location(BaseModel):
    country: str
    region: str | None = None
    remote_allowed: bool | None = None


class Source(BaseModel):
    type: SourceType
    origin: str
    last_fetched_at: date


class CreateScholarshipListingRequest(BaseModel):
    title: str
    description: str
    external_url: str
    eligibility_summary: str
    tags: list[str]
    provider: Provider
    location: Location
    source: Source
    money: Money | None = None
    deadline: date | None = None
