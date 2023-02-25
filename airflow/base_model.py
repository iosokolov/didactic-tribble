from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession

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
