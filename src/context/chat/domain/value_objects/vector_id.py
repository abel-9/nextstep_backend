# Base Id Class
from src.context.shared_kernel.domain.value_objects.id import Id


class VectorId(Id["VectorId"]):
    def __init__(self, value: str):
        super.__init__(value=value)
