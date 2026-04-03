from pydantic import BaseModel, ConfigDict, field_validator


class Money(BaseModel):
    amount: float
    currency: str

    model_config = ConfigDict(frozen=True)

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: float) -> float:
        if value < 0:
            raise ValueError("Amount cannot be negative.")
        return value

    @field_validator("currency")
    @classmethod
    def validate_currency(cls, value: str) -> str:
        normalized = value.strip().upper()
        if len(normalized) != 3:
            raise ValueError("Currency must be a 3-letter ISO code.")
        return normalized
