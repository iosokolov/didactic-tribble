from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

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
