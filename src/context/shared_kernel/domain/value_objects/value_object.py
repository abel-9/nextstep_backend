from typing import Generic, TypeVar, Any
from pydantic import BaseModel, ConfigDict

T = TypeVar("T")

class ValueObject(BaseModel, Generic[T]):
    """
    Base class for Value Objects in DDD.
    Value objects are defined by their attributes, not an identity.
    """
    value: T

    # Ensure immutability (Value Objects should not change after creation)
    model_config = ConfigDict(frozen=True)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ValueObject):
            return False
        return self.value == other.value

    def __str__(self) -> str:
        return str(self.value)
