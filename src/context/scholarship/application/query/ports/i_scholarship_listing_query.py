from abc import abstractmethod

from src.context.scholarship.application.query.read_models import (
    ScholarshipListingReadModel,
)
from src.context.scholarship.domain.enums import ListingStatus
from src.context.shared_kernel.domain.repository import Repository


class IScholarshipListingQuery(Repository[ScholarshipListingReadModel]):
    @abstractmethod
    async def get_by_status(
        self, status: ListingStatus
    ) -> list[ScholarshipListingReadModel]:
        pass
