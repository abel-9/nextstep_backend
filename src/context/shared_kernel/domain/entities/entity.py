from abc import ABC


class Entity[T](ABC):
    def __init__(self, id: T):
        self.__id = id
        self.__events: list[any] = []

    @property
    def id(self) -> T:
        return self.__id

    @property
    def events(self) -> list[any]:
        return self.__events

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False
        return self.id == other.id

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"
