from abc import ABC


class DocumentEntity(ABC):
    def __init__(self, vector: list[float]):
        self.__vector = vector

    @property
    def vector(self) -> list[float]:
        return self.__vector

    def update_vector(self, vector: list[float]):
        self.__vector = vector
