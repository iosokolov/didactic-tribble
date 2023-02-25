from asyncio import current_task
from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic.networks import PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy.orm import sessionmaker

import settings


class AsyncPostgresDsn(PostgresDsn):
    allowed_schemes = list(PostgresDsn.allowed_schemes) + ["postgresql+asyncpg"]


DB_URI = AsyncPostgresDsn.build(
    scheme="postgresql+asyncpg",
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    path=f"/{settings.POSTGRES_DB}",
)

engine = create_async_engine(
    DB_URI,
    pool_pre_ping=True,
    echo=settings.ECHO,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW
)

async_session = async_sessionmaker(engine)

# Session = async_scoped_session(
#     sessionmaker(
#         autocommit=False,
#         autoflush=False,
#         bind=engine,
#         expire_on_commit=False,
#         class_=AsyncSession,
#     ),
#     scopefunc=current_task
# )
# Session = async_scoped_session(
#     async_sessionmaker(autocommit=False, autoflush=False, bind=engine,  expire_on_commit=False, class_=AsyncSession),
#     scopefunc=current_task
# )
