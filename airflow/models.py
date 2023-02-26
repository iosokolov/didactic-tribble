import uuid
from typing import List, Dict

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
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import JSONB, insert
from sqlalchemy import select, update

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

    @classmethod
    async def bulk_upsert(cls, db: AsyncSession, items: List[dict]):
        query = insert(cls.__table__).values(items)
        query = query.on_conflict_do_update(
            index_elements=["code"],
            set_={
                "name": query.excluded.name,
            },
        )
        await db.execute(query)

    @classmethod
    async def select_mapping(
            cls,
            db: AsyncSession,
            **kwargs,
    ) -> Dict[str, int]:
        query = select(cls.id).filter_by(**kwargs)
        cur = await db.execute(query)
        items = cur.scalars().all()
        return {
            item['code']: item['id']
            for item in items
        }


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

    __table_args__ = (
        UniqueConstraint(
            currency_id, date,
            name="uix_rate_currency_id_date",
        ),
    )

    @classmethod
    async def bulk_upsert(cls, db: AsyncSession, items: List[dict]):
        query = insert(cls.__table__).values(items)
        query = query.on_conflict_do_update(
            index_elements=["currency_id", "date"],
            set_={
                "quant": query.excluded.quant,
                "quant_ktz": query.excluded.quant_ktz,
            },
        )
        await db.execute(query)
