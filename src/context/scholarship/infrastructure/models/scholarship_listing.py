from datetime import date

from beanie import Document
from pydantic import BaseModel, Field


class Provider(BaseModel):
    name: str
    website: str
    country: str
    verified: bool


class Money(BaseModel):
    amount: float
    currency: str


class Location(BaseModel):
    country: str
    region: str | None = None
    remote_allowed: bool | None = None


class Source(BaseModel):
    type: str
    origin: str
    last_fetched_at: date


class ScholarshipListing(Document):
    id: str = Field(alias="_id")
    title: str
    description: str
    provider: Provider
    external_url: str
    amount: Money | None = None
    deadline: date | None = None
    eligibility_summary: str
    tags: list[str] = []
    location: Location
    status: str
    source: Source
    created_at: date
    updated_at: date

    class Settings:
        name = "scholarship_listings"
