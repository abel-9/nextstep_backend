from src.context.scholarship.application.query.ports import IScholarshipListingQuery
from src.context.scholarship.application.query.queries import GetScholarshipListingQuery
from src.context.scholarship.application.query.read_models import (
    ScholarshipListingReadModel,
)


class GetScholarshipListingQueryHandler:
    def __init__(self, scholarship_listing_query: IScholarshipListingQuery):
        self.__scholarship_listing_query = scholarship_listing_query

    async def __call__(
        self, query: GetScholarshipListingQuery
    ) -> ScholarshipListingReadModel | None:
        return await self.__scholarship_listing_query.get_by_id(id=query.listing_id)
