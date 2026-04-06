from src.context.scholarship.domain.entities import (
    Provider as ScholarshipProvider,
    ScholarshipListing,
)
from src.context.scholarship.domain.enums import ListingStatus, SourceType
from src.context.scholarship.domain.value_object import (
    ListingId,
    Location,
    Money,
    Source,
    Url,
)
from src.context.scholarship.infrastructure.models import (
    LocationModel,
    MoneyModel,
    ProviderModel,
    ScholarshipListingModel,
    SourceModel,
)


class ScholarshipListingMapper:
    @staticmethod
    def to_beanie_scholarship_listing(
        scholarship_listing: ScholarshipListing,
    ) -> ScholarshipListingModel:
        amount = None
        if scholarship_listing.amount is not None:
            amount = MoneyModel(
                amount=scholarship_listing.amount.amount,
                currency=scholarship_listing.amount.currency,
            )

        return ScholarshipListingModel(
            id=scholarship_listing.id.value,
            title=scholarship_listing.title,
            description=scholarship_listing.description,
            provider=ProviderModel(
                name=scholarship_listing.provider.name,
                website=scholarship_listing.provider.website.value,
                country=scholarship_listing.provider.country,
                verified=scholarship_listing.provider.verified,
            ),
            external_url=scholarship_listing.external_url.value,
            amount=amount,
            deadline=scholarship_listing.deadline,
            eligibility_summary=scholarship_listing.eligibility_summary,
            tags=scholarship_listing.tags,
            location=LocationModel(
                country=scholarship_listing.location.country,
                region=scholarship_listing.location.region,
                remote_allowed=scholarship_listing.location.remote_allowed,
            ),
            status=scholarship_listing.status.value,
            source=SourceModel(
                type=scholarship_listing.source.type.value,
                origin=scholarship_listing.source.origin,
                last_fetched_at=scholarship_listing.source.last_fetched_at,
            ),
            created_at=scholarship_listing.created_at,
            updated_at=scholarship_listing.updated_at,
        )

    @staticmethod
    def from_beanie_scholarship_listing(
        scholarship_listing_model: ScholarshipListingModel,
    ) -> ScholarshipListing:
        amount = None
        if scholarship_listing_model.amount is not None:
            amount = Money(
                amount=scholarship_listing_model.amount.amount,
                currency=scholarship_listing_model.amount.currency,
            )

        return ScholarshipListing(
            id=ListingId(scholarship_listing_model.id),
            title=scholarship_listing_model.title,
            description=scholarship_listing_model.description,
            provider=ScholarshipProvider(
                name=scholarship_listing_model.provider.name,
                website=Url(scholarship_listing_model.provider.website),
                country=scholarship_listing_model.provider.country,
                verified=scholarship_listing_model.provider.verified,
            ),
            external_url=Url(scholarship_listing_model.external_url),
            amount=amount,
            deadline=scholarship_listing_model.deadline,
            eligibility_summary=scholarship_listing_model.eligibility_summary,
            tags=scholarship_listing_model.tags,
            location=Location(
                country=scholarship_listing_model.location.country,
                region=scholarship_listing_model.location.region,
                remote_allowed=scholarship_listing_model.location.remote_allowed,
            ),
            status=ListingStatus(scholarship_listing_model.status),
            source=Source(
                type=SourceType(scholarship_listing_model.source.type),
                origin=scholarship_listing_model.source.origin,
                last_fetched_at=scholarship_listing_model.source.last_fetched_at,
            ),
            created_at=scholarship_listing_model.created_at,
            updated_at=scholarship_listing_model.updated_at,
        )
