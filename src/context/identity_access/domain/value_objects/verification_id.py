# Base Value Object
from src.context.shared_kernel.domain.value_objects.id import Id


class VerificationId(Id["VerificationId"]):
    def __init__(self, value: str):
        super().__init__(value=value)
