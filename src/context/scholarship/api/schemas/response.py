from datetime import date

from pydantic import BaseModel


class CreateScholarshipListingResponse(BaseModel):
    message: str


class ScholarshipProviderResponse(BaseModel):
    name: str
    website: str
    country: str
    verified: bool


class ScholarshipMoneyResponse(BaseModel):
    amount: float
    currency: str


class ScholarshipLocationResponse(BaseModel):
    country: str
    region: str | None = None
    remote_allowed: bool | None = None


class ScholarshipSourceResponse(BaseModel):
    type: str
    origin: str
    last_fetched_at: date


class ScholarshipListingResponse(BaseModel):
    id: str
    title: str
    description: str
    provider: ScholarshipProviderResponse
    external_url: str
    amount: ScholarshipMoneyResponse | None = None
    deadline: date | None = None
    eligibility_summary: str
    tags: list[str]
    location: ScholarshipLocationResponse
    status: str
    source: ScholarshipSourceResponse
    created_at: date
    updated_at: date
