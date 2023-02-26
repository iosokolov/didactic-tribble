import uuid

from base_model import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    DateTime,
    DECIMAL,
    Table,
    Boolean,
    UniqueConstraint, Enum,
    ARRAY, text, bindparam
)
from sqlalchemy.dialects.postgresql import UUID

from constants import StatusEnum


class Record(Model):
    __tablename__ = 'record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    request_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False, index=True)
    status = Column("status", Enum(StatusEnum, name='status_enum'), nullable=False)


class Currency(Model):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(3), nullable=False)
    name = Column(String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint(code, name="uix_currency_code"),
    )


class Rate(Model):
    __tablename__ = 'rate'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    currency_id = Column(
        Integer,
        ForeignKey("currency.id", name="rate_currency_id_fkey"),
        nullable=False,
    )
    quant = Column(DECIMAL, nullable=False)
    quant_kzt = Column(DECIMAL, nullable=False)
