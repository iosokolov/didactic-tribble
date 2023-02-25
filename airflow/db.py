from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic.networks import PostgresDsn
from sqlalchemy.ext.asyncio import create_async_engine

import env_vars


class AsyncPostgresDsn(PostgresDsn):
    allowed_schemes = list(PostgresDsn.allowed_schemes) + ["postgresql+asyncpg"]


DB_URI = AsyncPostgresDsn.build(
    scheme="postgresql+asyncpg",
    user=env_vars.POSTGRES_USER,
    password=env_vars.POSTGRES_PASSWORD,
    host=env_vars.POSTGRES_HOST,
    port=env_vars.POSTGRES_PORT,
    path=f"/{env_vars.POSTGRES_DB}",
)

engine = create_async_engine(
    DB_URI,
    pool_pre_ping=True,
    echo=env_vars.ECHO,
    pool_size=env_vars.DB_POOL_SIZE,
    max_overflow=env_vars.DB_MAX_OVERFLOW,
)

session_maker = async_sessionmaker(engine)
