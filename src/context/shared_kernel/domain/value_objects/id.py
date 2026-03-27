import uuid

from src.context.shared_kernel.domain.value_objects.value_object import ValueObject

class Id[T](ValueObject[str]):
    def __init__(self, value: str):
        super().__init__(value=value)
    
    @classmethod
    def generate(cls) -> T:
        id = str(uuid.uuid4())
        return cls(value=id)