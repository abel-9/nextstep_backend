from dataclasses import dataclass
from datetime import date

from src.context.scholarship.domain.enums import SourceType


@dataclass
class Money:
    amount: float
    currency: str


@dataclass
class Provider:
    name: str
    website: str
    country: str
    verified: bool


@dataclass
class Location:
    country: str
    region: str | None = None
    remote_allowed: bool | None = None


@dataclass
class Source:
    type: SourceType
    origin: str
    last_fetched_at: date


@dataclass
class CreateScholarshipListingCommand:
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
