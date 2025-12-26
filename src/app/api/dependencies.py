from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from core.db.database import async_session

# Define an async function to get the database session
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
  """Dependency to provice the async session object"""
  async with async_session() as session:
    yield session
              
AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]