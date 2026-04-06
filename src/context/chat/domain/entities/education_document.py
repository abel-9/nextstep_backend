# Shared Base Entity
from src.context.chat.domain.entities.document_entity import DocumentEntity
from src.context.shared_kernel.domain.entities.entity import Entity

# Value Objects
from src.context.chat.domain.value_objects import (
    EducationMetadata,
    VectorId,
)


class EducationDocument(Entity[VectorId], DocumentEntity):
    def __init__(
        self,
        id: VectorId,
        vector: list[float],
        education_metadata: EducationMetadata,
    ):
        Entity.__init__(self, id)
        DocumentEntity.__init__(self, vector=vector)
        self.__metadata = education_metadata

    @property
    def metadata(self) -> EducationMetadata:
        return self.__metadata

    @classmethod
    def create(
        cls, vector: list[float], education_metadata: EducationMetadata
    ) -> "EducationDocument":
        id = VectorId.generate()
        return cls(id=id, vector=vector, education_metadata=education_metadata)

    def update_metadata(self, metadata: EducationMetadata, vector: list[float]):
        self.__metadata = metadata
        self.update_vector(vector=vector)

    def content(self) -> str:
        return self.__metadata.to_content()
