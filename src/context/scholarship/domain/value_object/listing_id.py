from src.context.shared_kernel.domain.value_objects.id import Id


class ListingId(Id["ListingId"]):
    def __init__(self, value: str):
        super().__init__(value=value)
