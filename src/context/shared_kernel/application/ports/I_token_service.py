from abc import ABC, abstractmethod


class ITokenService(ABC):
    @abstractmethod
    async def sign(self, payload: dict) -> str:
        pass

    @abstractmethod
    async def verify(self, token: str) -> dict:
        pass
