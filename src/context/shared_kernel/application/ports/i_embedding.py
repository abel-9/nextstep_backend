from abc import ABC, abstractmethod
from typing import List


class IEmbedding(ABC):
    @abstractmethod
    async def embed(self, text: str) -> List[float]:
        pass
