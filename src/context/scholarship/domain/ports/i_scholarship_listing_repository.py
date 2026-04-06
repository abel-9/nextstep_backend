from abc import abstractmethod

from src.context.scholarship.domain.entities import ScholarshipListing
from src.context.scholarship.domain.enums import ListingStatus
from src.context.scholarship.domain.value_object import Url
from src.context.shared_kernel.domain.repository import Repository


class IScholarshipListingRepository(Repository[ScholarshipListing]):
    @abstractmethod
    async def get_by_external_url(self, external_url: Url) -> ScholarshipListing | None:
        pass

    @abstractmethod
    async def get_by_status(self, status: ListingStatus) -> list[ScholarshipListing]:
        pass
