from src.context.chat.application.command.commands import CreateWorkExperienceCommand
from src.context.chat.domain.entities import ProfileAggregate
from src.context.chat.domain.ports import IProfileDocumentRepository
from src.context.chat.domain.value_objects import (
    ProfileId,
    UserId,
    WorkExperienceMetadata,
)
from src.context.shared_kernel.application.ports import IEmbedding


class CreateWorkExperienceDocumentUseCase:
    def __init__(
        self,
        profile_document_repository: IProfileDocumentRepository,
        embedding: IEmbedding,
    ):
        self.__profile_document_repository = profile_document_repository
        self.__embedding = embedding

    async def __call__(self, cmd: CreateWorkExperienceCommand):
        metadata = WorkExperienceMetadata(
            work_experience_id=cmd.work_experience_id,
            profile_id=cmd.profile_id,
            user_id=cmd.user_id,
            company=cmd.company,
            position=cmd.position,
            description=cmd.description,
        )
        vector = await self.__embedding.embed(text=metadata.to_content())

        aggregate = await self.__profile_document_repository.get_by_profile_id(
            profile_id=cmd.profile_id,
            user_id=cmd.user_id,
        )

        if not aggregate:
            aggregate = ProfileAggregate.create(
                profile_id=ProfileId(value=cmd.profile_id),
                user_id=UserId(value=cmd.user_id),
                education_documents=[],
                work_experience_documents=[],
            )
            aggregate.upsert_work_experience(metadata=metadata, vector=vector)
            profile_vector = await self.__embedding.embed(
                text=aggregate.compose_profile_content()
            )
            aggregate.upsert_profile_document(vector=profile_vector)
            await self.__profile_document_repository.save(aggregate)
            return

        aggregate.upsert_work_experience(metadata=metadata, vector=vector)
        profile_vector = await self.__embedding.embed(
            text=aggregate.compose_profile_content()
        )
        aggregate.upsert_profile_document(vector=profile_vector)
        await self.__profile_document_repository.update(aggregate)
