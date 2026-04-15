from src.context.chat.domain.entities.document_entity import DocumentEntity
from src.context.chat.domain.value_objects import VectorId, WorkExperienceMetadata
from src.context.shared_kernel.domain.entities.entity import Entity


class WorkExperienceDocument(Entity[VectorId], DocumentEntity):
    def __init__(
        self,
        id: VectorId,
        vector: list[float],
        work_experience_metadata: WorkExperienceMetadata,
    ):
        Entity.__init__(self, id)
        DocumentEntity.__init__(self, vector=vector)
        self.__metadata = work_experience_metadata

    @property
    def metadata(self) -> WorkExperienceMetadata:
        return self.__metadata

    @classmethod
    def create(
        cls,
        vector: list[float],
        work_experience_metadata: WorkExperienceMetadata,
    ) -> "WorkExperienceDocument":
        id = VectorId.generate()
        return cls(
            id=id,
            vector=vector,
            work_experience_metadata=work_experience_metadata,
        )

    def update_metadata(self, metadata: WorkExperienceMetadata, vector: list[float]):
        self.__metadata = metadata
        self.update_vector(vector=vector)

    def content(self) -> str:
        return self.__metadata.to_content()
