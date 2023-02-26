import enum


class StatusEnum(str, enum.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class CurrencyEnum(str, enum.Enum):
    KZT = "KZT"
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"
