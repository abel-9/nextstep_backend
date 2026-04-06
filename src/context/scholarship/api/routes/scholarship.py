from fastapi import APIRouter, Request, status

from src.context.scholarship.api.schemas.request import CreateScholarshipListingRequest
from src.context.scholarship.api.schemas.response import (
    CreateScholarshipListingResponse,
    ScholarshipListingResponse,
)
from src.context.scholarship.application.command.commands import (
    CreateScholarshipListingCommand,
    Location as CommandLocation,
    Money as CommandMoney,
    Provider as CommandProvider,
    Source as CommandSource,
)
from src.context.scholarship.application.query.queries import (
    GetScholarshipListingQuery,
    GetScholarshipListingsQuery,
)
from src.context.scholarship.domain.enums import ListingStatus

router = APIRouter(prefix="/scholarship")


@router.post(
    "",
    response_model=CreateScholarshipListingResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_scholarship_listing(
    req: CreateScholarshipListingRequest,
    request: Request,
):
    money = None
    if req.money is not None:
        money = CommandMoney(amount=req.money.amount, currency=req.money.currency)

    cmd = CreateScholarshipListingCommand(
        title=req.title,
        description=req.description,
        external_url=req.external_url,
        eligibility_summary=req.eligibility_summary,
        tags=req.tags,
        provider=CommandProvider(
            name=req.provider.name,
            website=req.provider.website,
            country=req.provider.country,
            verified=req.provider.verified,
        ),
        location=CommandLocation(
            country=req.location.country,
            region=req.location.region,
            remote_allowed=req.location.remote_allowed,
        ),
        source=CommandSource(
            type=req.source.type,
            origin=req.source.origin,
            last_fetched_at=req.source.last_fetched_at,
        ),
        money=money,
        deadline=req.deadline,
    )
    await request.app.state.container.mediator.send(request=cmd)


@router.get("", response_model=list[ScholarshipListingResponse])
async def get_scholarship_listings(
    request: Request,
    status: ListingStatus | None = None,
):
    query = GetScholarshipListingsQuery(status=status)
    return await request.app.state.container.mediator.send(request=query)


@router.get("/{listing_id}", response_model=ScholarshipListingResponse | None)
async def get_scholarship_listing(
    listing_id: str,
    request: Request,
):
    query = GetScholarshipListingQuery(listing_id=listing_id)
    return await request.app.state.container.mediator.send(request=query)
