from src.context.chat.application.command.commands import (
    CreateScholarshipDocumentCommand,
)
from src.context.chat.domain.entities import ScholarshipAggregate
from src.context.chat.domain.ports import IScholarshipDocumentRepository
from src.context.chat.domain.value_objects import ScholarshipMetadata
from src.context.shared_kernel.application.ports import IEmbedding


class CreateScholarshipDocumentUseCase:
    def __init__(
        self,
        scholarship_document_repository: IScholarshipDocumentRepository,
        embedding: IEmbedding,
    ):
        self.__scholarship_document_repository = scholarship_document_repository
        self.__embedding = embedding

    async def __call__(self, cmd: CreateScholarshipDocumentCommand):
        metadata = ScholarshipMetadata(
            listing_id=cmd.listing_id,
            title=cmd.title,
            description=cmd.description,
            eligibility_summary=cmd.eligibility_summary,
            provider_name=cmd.provider_name,
            tags=cmd.tags,
            deadline=cmd.deadline,
        )
        vector = await self.__embedding.embed(text=metadata.to_content())

        aggregate = await self.__scholarship_document_repository.get_by_listing_id(
            listing_id=cmd.listing_id
        )

        if not aggregate:
            aggregate = ScholarshipAggregate.create(listing_id=cmd.listing_id)
            aggregate.upsert_document(metadata=metadata, vector=vector)
            await self.__scholarship_document_repository.save(aggregate)
            return

        aggregate.upsert_document(metadata=metadata, vector=vector)
        await self.__scholarship_document_repository.update(aggregate)
