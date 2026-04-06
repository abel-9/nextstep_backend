from abc import ABC, abstractmethod


class Metadata(ABC):
    @abstractmethod
    def to_content(self) -> str:
        pass
