import google.generativeai as genai

# Settings
from src.core.settings import settings

# Interface
from src.context.shared_kernel.application.ports.i_embedding import IEmbedding


class GeminiEmbedding001(IEmbedding):
    def __init__(self):
        self.genai = genai
        self.genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = "models/gemini-embedding-001"
        self.task_type = "retrieval_document"
        self.title = "Embedding Request"
        self.output_dimensionality = 512

    async def embed(self, text: str) -> list[float]:
        result = self.genai.embed_content(
            model=self.model,
            content=text,
            task_type=self.task_type,
            title=self.title,
            output_dimensionality=self.output_dimensionality,
        )
        return result["embedding"]
