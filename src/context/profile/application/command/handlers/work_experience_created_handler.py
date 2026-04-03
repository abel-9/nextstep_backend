# Events
from src.context.profile.domain.events import WorkExperienceCreated

# Dependencies
from src.context.shared_kernel.application.ports import (
    IEmbedding,
    IDocumentVectorRepository,
)


class WorkExperienceCreatedHandler:
    def __init__(
        self,
        embedding_service: IEmbedding,
        document_vector_repository: IDocumentVectorRepository,
    ):
        self.__embedding_service = embedding_service
        self.__document_vector_repository = document_vector_repository

    async def __call__(self, event: WorkExperienceCreated):
        # Generate an embedding for the work experience description
        embedding = await self.__embedding_service.embed(event.description)

        await self.__document_vector_repository.add_vector(
            document_id=event.id,
            vector=embedding,
        )
