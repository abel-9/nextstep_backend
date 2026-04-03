# Events
from src.context.profile.domain.events import WorkExperienceCreated

# Dependencies
from src.context.shared_kernel.application.ports import IEmbedding, IVectorDB


class WorkExperienceCreatedHandler:
    def __init__(self, embedding_service: IEmbedding, vector_db: IVectorDB):
        self.__embedding_service = embedding_service
        self.__vector_db = vector_db

    async def __call__(self, event: WorkExperienceCreated):
        # Generate an embedding for the work experience description
        embedding = await self.__embedding_service.embed(event.description)

        # Here you would typically save the embedding to your database
        # associated with the work experience record. This is just a placeholder.
        print(
            f"Generated embedding for work experience {event.id}: {embedding[:5]}..."
        )  # Print first 5 values for brevity
