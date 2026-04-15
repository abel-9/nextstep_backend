from dataclasses import dataclass


@dataclass(frozen=True)
class CreateScholarshipDocumentCommand:
    listing_id: str
    title: str
    description: str
    eligibility_summary: str
    provider_name: str
    tags: list[str]
    deadline: str | None
