from src.context.scholarship.domain.entities import ScholarshipListing
from src.context.scholarship.domain.enums import ListingStatus
from src.context.scholarship.domain.ports import IScholarshipListingRepository
from src.context.scholarship.domain.value_object import Url
from src.context.scholarship.infrastructure.mappers import ScholarshipListingMapper
from src.context.scholarship.infrastructure.models import ScholarshipListingModel


class ScholarshipListingBeanieRepository(IScholarshipListingRepository):
    async def get_all(self, query=None) -> list[ScholarshipListing]:
        scholarship_listing_models = await ScholarshipListingModel.find_all().to_list()
        return [
            ScholarshipListingMapper.from_beanie_scholarship_listing(
                scholarship_listing_model
            )
            for scholarship_listing_model in scholarship_listing_models
        ]

    async def get_by_id(self, id: str) -> ScholarshipListing | None:
        scholarship_listing_model = await ScholarshipListingModel.find_one(
            ScholarshipListingModel.id == id
        )
        if scholarship_listing_model:
            return ScholarshipListingMapper.from_beanie_scholarship_listing(
                scholarship_listing_model
            )
        return None

    async def save(self, entity: ScholarshipListing) -> None:
        scholarship_listing_model = (
            ScholarshipListingMapper.to_beanie_scholarship_listing(entity)
        )
        await scholarship_listing_model.insert()

    async def update(self, entity: ScholarshipListing) -> None:
        scholarship_listing_model = (
            ScholarshipListingMapper.to_beanie_scholarship_listing(entity)
        )
        await scholarship_listing_model.replace()

    async def remove(self, entity: ScholarshipListing) -> None:
        scholarship_listing_model = await ScholarshipListingModel.find_one(
            ScholarshipListingModel.id == entity.id.value
        )
        if scholarship_listing_model:
            await scholarship_listing_model.delete()

    async def get_by_external_url(self, external_url: Url) -> ScholarshipListing | None:
        scholarship_listing_model = await ScholarshipListingModel.find_one(
            ScholarshipListingModel.external_url == external_url.value
        )
        if scholarship_listing_model:
            return ScholarshipListingMapper.from_beanie_scholarship_listing(
                scholarship_listing_model
            )
        return None

    async def get_by_status(self, status: ListingStatus) -> list[ScholarshipListing]:
        scholarship_listing_models = await ScholarshipListingModel.find(
            ScholarshipListingModel.status == status.value
        ).to_list()
        return [
            ScholarshipListingMapper.from_beanie_scholarship_listing(
                scholarship_listing_model
            )
            for scholarship_listing_model in scholarship_listing_models
        ]
