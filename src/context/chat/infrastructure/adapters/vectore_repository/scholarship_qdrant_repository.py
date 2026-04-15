from qdrant_client.http import models

from src.core.interfaces import IVectorDB
from src.context.chat.domain.entities import ScholarshipAggregate
from src.context.chat.domain.ports import IScholarshipDocumentRepository
from src.context.chat.domain.enums import PointKindEnums
from src.context.chat.infrastructure.mappers import ScholarshipQdrantMapper


class ScholarshipQdrantRepository(IScholarshipDocumentRepository):
    def __init__(self, vector_db: IVectorDB):
        self.__vector_db = vector_db

    async def get_by_listing_id(self, listing_id: str) -> ScholarshipAggregate | None:
        client = self.__vector_db.get_client()
        points, _ = await client.scroll(
            collection_name=self.__vector_db.collection_name,
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="kind",
                        match=models.MatchValue(value=PointKindEnums.SCHOLARSHIP.value),
                    ),
                    models.FieldCondition(
                        key="listing_id",
                        match=models.MatchValue(value=listing_id),
                    ),
                ]
            ),
            with_payload=True,
            with_vectors=True,
            limit=1,
        )

        if not points:
            return None

        return ScholarshipQdrantMapper.from_qdrant_points(
            points=points,
            listing_id=listing_id,
        )

    async def save(self, scholarship_aggregate: ScholarshipAggregate) -> None:
        await self.__upsert_document(scholarship_aggregate)

    async def update(self, scholarship_aggregate: ScholarshipAggregate) -> None:
        await self.__upsert_document(scholarship_aggregate)

    async def __upsert_document(self, aggregate: ScholarshipAggregate) -> None:
        points = ScholarshipQdrantMapper.to_qdrant_points(aggregate=aggregate)
        if not points:
            return

        client = self.__vector_db.get_client()
        await client.upsert(
            collection_name=self.__vector_db.collection_name,
            points=points,
        )
