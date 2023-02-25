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


class Record(Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)

