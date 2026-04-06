from src.context.scholarship.application.query.ports import IScholarshipListingQuery
from src.context.scholarship.application.query.queries import (
    GetScholarshipListingsQuery,
)
from src.context.scholarship.application.query.read_models import (
    ScholarshipListingReadModel,
)


class GetScholarshipListingsQueryHandler:
    def __init__(self, scholarship_listing_query: IScholarshipListingQuery):
        self.__scholarship_listing_query = scholarship_listing_query

    async def __call__(
        self, query: GetScholarshipListingsQuery
    ) -> list[ScholarshipListingReadModel]:
        if query.status is None:
            return await self.__scholarship_listing_query.get_all(query=None)
        return await self.__scholarship_listing_query.get_by_status(status=query.status)
