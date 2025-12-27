from fastapi import (
  APIRouter,
  status
)

from api.dependencies import AsyncSessionDep 

from core.schemas.users import User, UserBase, UserCreate
from crud import CRUDBase


router = APIRouter(tags=["User"])


@router.post("",
  response_model=User,
  status_code=status.HTTP_201_CREATED,
  operation_id="createUser")
async def create_user(
  user_create: UserCreate,
  session: AsyncSessionDep
):
  user = await CRUDBase(session, User).create(user_create)
  return user

@router.get("/me",
  response_model=UserBase,
  status_code=status.HTTP_200_OK,
  operation_id="getCurrentUser")
async def get_active_user():
  pass