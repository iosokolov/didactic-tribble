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
