#Base Value Object
from src.context.shared_kernel.domain.value_objects.value_object import ValueObject
#Enums
from src.context.identity_access.domain.enums.provider_enums import ProviderEnums

class Provider(ValueObject[ProviderEnums]):
    def __init__(self, value: ProviderEnums):
        
        if not isinstance(value, ProviderEnums):
            raise ValueError(f"Invalid provider: {value}. Must be a member of ProviderEnums.")
        super().__init__(value=value)