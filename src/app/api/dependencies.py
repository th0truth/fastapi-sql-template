from typing import Annotated, AsyncGenerator

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from sqlmodel.ext.asyncio.session import AsyncSession

from core.security.jwt import OAuthJWTBearer
from core.db.database import async_session

from core.config import settings

# OAuth2 scheme for authentication
oauth2_scheme = OAuth2PasswordBearer(
  tokenUrl=f"{settings.API_V1_STR}/auth/login",
)

# Define an async function to get the database session
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
  """Dependency to provice the async session object"""
  async with async_session() as session:
    yield session
              
AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]


async def get_current_user(
  token: Annotated[str, Depends()],  
  security_scopes: SecurityScopes
):
  # Decode the user JWT
  if not (payload := OAuthJWTBearer.decode(token=token)):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid or expired token.",
      headers={"WWW-Authenticate": "Bearer"},
    )
  

  # Get data from payload
  username, jti = payload.get("sub"), payload.get("jti")

  