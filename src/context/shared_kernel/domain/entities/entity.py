from abc import ABC


class Entity[T](ABC):
    def __init__(self, id: T):
        self.__id = id
    
    @property
    def id(self) -> T:
        return self.__id
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False
        return self.id == other.id
    
    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id})'
        
        