import random
from src.context.shared_kernel.application.ports.i_embedding import IEmbedding


class FakeEmbedding(IEmbedding):
    def __init__(self):
        # Match your real model's dimension so the DB doesn't crash
        self.output_dimensionality = 512

    async def embed(self, text: str) -> list[float]:
        """
        Returns a list of 512 random floats between -1 and 1.
        No API call is made.
        """
        # Generating deterministic 'fake' vectors can help with tests,
        # but random is fine for a basic mock.
        return [random.uniform(-1, 1) for _ in range(self.output_dimensionality)]
