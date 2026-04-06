from src.context.scholarship.application.command.commands import (
    CreateScholarshipListingCommand,
)
from src.context.scholarship.domain.entities import Provider, ScholarshipListing
from src.context.scholarship.domain.ports import IScholarshipListingRepository
from src.context.scholarship.domain.value_object import (
    Location,
    Money,
    Source,
    Url,
)


class CreateScholarshipListingUseCase:
    def __init__(self, listing_repository: IScholarshipListingRepository):
        self.__listing_repository = listing_repository

    async def __call__(self, cmd: CreateScholarshipListingCommand) -> None:
        await self.execute(cmd=cmd)

    async def execute(self, cmd: CreateScholarshipListingCommand) -> None:
        provider = Provider(
            name=cmd.provider.name,
            website=Url(cmd.provider.website),
            country=cmd.provider.country,
            verified=cmd.provider.verified,
        )

        source = Source(
            type=cmd.source.type,
            origin=cmd.source.origin,
            last_fetched_at=cmd.source.last_fetched_at,
        )

        amount = None
        if cmd.money is not None:
            amount = Money(amount=cmd.money.amount, currency=cmd.money.currency)

        listing = ScholarshipListing.create(
            title=cmd.title,
            description=cmd.description,
            provider=provider,
            external_url=Url(cmd.external_url),
            amount=amount,
            deadline=cmd.deadline,
            eligibility_summary=cmd.eligibility_summary,
            tags=cmd.tags,
            location=Location(
                country=cmd.location.country,
                region=cmd.location.region,
                remote_allowed=cmd.location.remote_allowed,
            ),
            source=source,
        )
        await self.__listing_repository.save(listing)
