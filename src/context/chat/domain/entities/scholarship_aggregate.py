from src.context.chat.domain.entities.scholarship_document import ScholarshipDocument
from src.context.chat.domain.value_objects import ScholarshipMetadata


class ScholarshipAggregate:
    def __init__(
        self,
        listing_id: str,
        document: ScholarshipDocument | None,
    ):
        self.__listing_id = listing_id
        self.__document = document

    @property
    def listing_id(self) -> str:
        return self.__listing_id

    @property
    def document(self) -> ScholarshipDocument | None:
        return self.__document

    @classmethod
    def create(cls, listing_id: str) -> "ScholarshipAggregate":
        return cls(listing_id=listing_id, document=None)

    def upsert_document(
        self,
        metadata: ScholarshipMetadata,
        vector: list[float],
    ) -> None:
        if metadata.listing_id != self.__listing_id:
            raise Exception("Scholarship listing mismatch")

        if self.__document:
            self.__document.update_metadata(metadata=metadata, vector=vector)
            return

        self.__document = ScholarshipDocument.create(
            vector=vector,
            scholarship_metadata=metadata,
        )
