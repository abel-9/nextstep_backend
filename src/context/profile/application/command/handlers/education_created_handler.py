# Events
from src.context.profile.domain.events import EducationCreated

# Dependencies
from src.context.shared_kernel.application.ports import (
    IEmbedding,
    IDocumentVectorRepository,
)


class EducationCreatedHandler:
    def __init__(
        self,
        embedding_service: IEmbedding,
        document_vector_repository: IDocumentVectorRepository,
    ):
        self.__embedding_service = embedding_service
        self.__document_vector_repository = document_vector_repository

    async def __call__(self, event: EducationCreated):
        # Generate an embedding for the education description
        embedding = await self.__embedding_service.embed(event.description)

        await self.__document_vector_repository.add_vector(
            document_id=event.id,
            vector=embedding,
            # metadata={
            #     "profile_id": event.profile_id,
            #     "type": "education",
            #     "institution": event.institution,
            #     "degree": event.degree,
            #     "field_of_study": event.field_of_study,
            #     "start_date": event.start_date.isoformat(),
            #     "end_date": event.end_date.isoformat()
            #     if event.end_date
            #     else None,
            # },
        )
