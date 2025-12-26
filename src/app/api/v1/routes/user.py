from fastapi import (
  APIRouter,
  status
)

from api.dependencies import AsyncSessionDep 

from core.schemas.users import User, UserCreate


router = APIRouter(tags=["User"])

@router.post("",
  status_code=status.HTTP_201_CREATED,
  operation_id="createUser",
  response_model=User)
async def create_user(
  user_create: UserCreate,
  session: AsyncSessionDep
):
  user = User.model_validate(user_create)
  session.add(user)
  await session.commit()
  await session.refresh(user)
  return user