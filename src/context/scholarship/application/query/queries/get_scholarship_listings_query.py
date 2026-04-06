from dataclasses import dataclass

from src.context.scholarship.domain.enums import ListingStatus


@dataclass
class GetScholarshipListingsQuery:
    status: ListingStatus | None = None
