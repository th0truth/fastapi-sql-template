from sqlalchemy.ext.asyncio import (
  AsyncSession,
  async_sessionmaker,
  create_async_engine
)

# Local Dependencies
from core.config import settings

# Create an async engine instance
async_engine = create_async_engine(
  url=f"postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOST}:{settings.POSTGRESQL_PORT}/{settings.POSTGRESQL_DBNAME}",
  echo=True,
  pool_pre_ping=True)

# Create a reusable Session class for consistent database interactions 
async_session = async_sessionmaker(
  async_engine,
  class_=AsyncSession,
  expire_on_commit=False,
  autoflush=False
)