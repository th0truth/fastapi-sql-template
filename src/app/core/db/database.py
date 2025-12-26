from sqlalchemy.ext.asyncio import (
  AsyncSession,
  async_sessionmaker,
  create_async_engine
)

# Local Dependencies
from core.config import settings

# Create an async engine instance
async_engine = create_async_engine(
  f"postgresql+psycopg2://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_PASSWORD}:{settings.POSTGRESQL_PORT}/{settings.POSTGRESQL_USER}?sslmode=require",
  echo=True,
  pool_pre_ping=True)

# Create a reusable Session class for consistent database interactions 
async_session = async_sessionmaker(
  async_engine,
  class_=AsyncSession,
  expire_on_commit=False,
  autoflush=False
)