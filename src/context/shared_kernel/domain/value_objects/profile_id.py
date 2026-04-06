# Base Class
from src.context.shared_kernel.domain.value_objects.id import Id


class ProfileId(Id["ProfileId"]):
    def __init__(self, value):
        super().__init__(value=value)
