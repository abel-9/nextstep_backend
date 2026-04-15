from src.context.chat.domain.entities.document_entity import DocumentEntity
from src.context.chat.domain.value_objects import ScholarshipMetadata, VectorId
from src.context.shared_kernel.domain.entities.entity import Entity


class ScholarshipDocument(Entity[VectorId], DocumentEntity):
    def __init__(
        self,
        id: VectorId,
        vector: list[float],
        scholarship_metadata: ScholarshipMetadata,
    ):
        Entity.__init__(self, id)
        DocumentEntity.__init__(self, vector=vector)
        self.__metadata = scholarship_metadata

    @property
    def metadata(self) -> ScholarshipMetadata:
        return self.__metadata

    @classmethod
    def create(
        cls, vector: list[float], scholarship_metadata: ScholarshipMetadata
    ) -> "ScholarshipDocument":
        return cls(
            id=VectorId.generate(),
            vector=vector,
            scholarship_metadata=scholarship_metadata,
        )

    def update_metadata(self, metadata: ScholarshipMetadata, vector: list[float]):
        self.__metadata = metadata
        self.update_vector(vector=vector)

    def content(self) -> str:
        return self.__metadata.to_content()
