# Interface
from src.context.shared_kernel.application.ports import IDocumentVectorRepository


class DocumentVectorRepository(IDocumentVectorRepository):
    def __init__(self, vector_db):
        self.vector_db = vector_db

    async def add_vector(self, document_id: str, vector: list[float]) -> None:
        client = self.vector_db.get_client()
        await client.upsert(
            collection_name=self.vector_db.collection_name,
            points=[
                {
                    "id": document_id,
                    "vector": vector,
                }
            ],
        )

    async def get_vector(self, document_id: str) -> list[float] | None:
        client = self.vector_db.get_client()
        try:
            response = await client.retrieve(
                collection_name=self.vector_db.collection_name,
                ids=[document_id],
            )
            if response.result and response.result.points:
                return response.result.points[0].vector
            return None
        except Exception as e:
            print(f"Error retrieving vector for document {document_id}: {e}")
            return None

    async def delete_vector(self, document_id: str) -> None:
        client = self.vector_db.get_client()
        await client.delete(
            collection_name=self.vector_db.collection_name,
            points_selector={"ids": [document_id]},
        )
