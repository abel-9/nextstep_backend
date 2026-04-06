# Interface
from src.context.scholarship.application.query.ports import IScholarshipListingQuery

# Read Models
from src.context.scholarship.application.query.read_models import (
    ScholarshipListingReadModel,
)

# Domain Enums
from src.context.scholarship.domain.enums import ListingStatus

# Beanie Models
from src.context.scholarship.infrastructure.models import ScholarshipListingModel


class ScholarshipListingBeanieQuery(IScholarshipListingQuery):
    async def get_all(self, query=None) -> list[ScholarshipListingReadModel]:
        listings = (
            await ScholarshipListingModel.find_all()
            .project(ScholarshipListingReadModel)
            .to_list()
        )
        return listings

    async def get_by_id(self, id: str) -> ScholarshipListingReadModel | None:
        listing = await ScholarshipListingModel.find_one(
            ScholarshipListingModel.id == id
        ).project(ScholarshipListingReadModel)
        return listing

    async def save(self, entity):
        pass

    async def update(self, entity):
        pass

    async def remove(self, entity):
        pass

    async def get_by_status(
        self, status: ListingStatus
    ) -> list[ScholarshipListingReadModel]:
        listings = (
            await ScholarshipListingModel.find(
                ScholarshipListingModel.status == status.value
            )
            .project(ScholarshipListingReadModel)
            .to_list()
        )
        return listings
