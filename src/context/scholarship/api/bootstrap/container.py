from functools import lru_cache

# core Container
from src.core.container import AppContainer

# shared container
from src.context.shared_kernel.bootstrap.container import SharedContainer

from src.context.scholarship.domain.ports import IScholarshipListingRepository
from src.context.scholarship.application.query.ports import IScholarshipListingQuery

from src.context.scholarship.infrastructure.adapters.repository import (
    ScholarshipListingBeanieRepository,
)
from src.context.scholarship.infrastructure.adapters.query import (
    ScholarshipListingBeanieQuery,
)

from src.context.scholarship.application.command.use_case import (
    CreateScholarshipListingUseCase,
)
from src.context.scholarship.application.query.handlers import (
    GetScholarshipListingQueryHandler,
    GetScholarshipListingsQueryHandler,
)


class ScholarshipContainer:
    def __init__(self, app_container: AppContainer, shared_container: SharedContainer):
        self.app_container = app_container
        self.shared_container = shared_container

    @lru_cache()
    def get_scholarship_listing_repository(self) -> IScholarshipListingRepository:
        return ScholarshipListingBeanieRepository()

    @lru_cache()
    def get_scholarship_listing_query(self) -> IScholarshipListingQuery:
        return ScholarshipListingBeanieQuery()

    @lru_cache()
    def get_create_scholarship_listing_use_case(
        self,
    ) -> CreateScholarshipListingUseCase:
        return CreateScholarshipListingUseCase(
            listing_repository=self.get_scholarship_listing_repository()
        )

    @lru_cache()
    def get_scholarship_listing_query_handler(
        self,
    ) -> GetScholarshipListingQueryHandler:
        return GetScholarshipListingQueryHandler(
            scholarship_listing_query=self.get_scholarship_listing_query()
        )

    @lru_cache()
    def get_scholarship_listings_query_handler(
        self,
    ) -> GetScholarshipListingsQueryHandler:
        return GetScholarshipListingsQueryHandler(
            scholarship_listing_query=self.get_scholarship_listing_query()
        )
