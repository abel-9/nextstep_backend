from src.context.shared_kernel.domain.value_objects.value_object import ValueObject

class EmailStr(ValueObject[str]):
    def __init__(self, value: str):
        super().__init__(value=value)