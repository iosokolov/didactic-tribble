from typing import Optional, List

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.sql.elements import BinaryExpression

Base = declarative_base()


class Model(Base):
    __abstract__ = True

    @classmethod
    async def create(
            cls,
            session: AsyncSession,
            data: dict,
    ):
        data.pop("id", None)
        instance = cls(**data)
        session.add(instance)
        await session.flush()
        return instance

    @classmethod
    async def select_one_or_none(
            cls,
            db: AsyncSession,
            **kwargs,
    ):
        query = select(cls).filter_by(**kwargs)
        cur = await db.execute(query)
        return cur.scalar_one_or_none()

    @classmethod
    async def select_all(
            cls,
            db: AsyncSession,
            expressions: Optional[List[BinaryExpression]] = None,
            **kwargs,
    ) -> list:
        query = select(cls)
        for expression in expressions or []:
            query = query.filter(expression)

        for column_name, value in kwargs.items():
            if isinstance(value, list):
                column = getattr(cls, column_name)
                query = query.filter(column.in_(value))
            else:
                query = query.filter_by(**{column_name: value})

        cur = await db.execute(query)
        return cur.scalars().all()
