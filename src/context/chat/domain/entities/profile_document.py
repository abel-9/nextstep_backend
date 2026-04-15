# Base entity
from src.context.shared_kernel.domain.entities.entity import Entity

# Base document entity
from src.context.chat.domain.entities.document_entity import DocumentEntity

# Value objects
from src.context.chat.domain.value_objects import VectorId, ProfileMetadata


class ProfileDocument(Entity[VectorId], DocumentEntity):
    def __init__(self, id: VectorId, vector: list[float], metadata: ProfileMetadata):
        Entity.__init__(self, id)
        DocumentEntity.__init__(self, vector=vector)
        self.__metadata = metadata

    @property
    def metadata(self) -> ProfileMetadata:
        return self.__metadata

    def update_metadata(self, metadata: ProfileMetadata, vector: list[float]):
        self.__metadata = metadata
        self.update_vector(vector=vector)

    def content(self) -> str:
        return self.__metadata.to_content()

    @classmethod
    def create(
        cls, vector: list[float], metadata: ProfileMetadata
    ) -> "ProfileDocument":
        return cls(
            id=VectorId.generate(),
            vector=vector,
            metadata=metadata,
        )
