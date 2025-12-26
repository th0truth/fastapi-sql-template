from typing import Annotated
from fastapi import (
  HTTPException,
  APIRouter,
  status,
  Depends,
  Body
)

router = APIRouter(tags=["User"])


@router.get("/me",
  status_code=status.HTTP_200_OK,
  response_model_exclude_none=True)
async def get_active_user(
  # user: Annotated[dict, Depends(get_current_user)]
):
  """
  Returns user data.
  """
  return {"hello": "worls"}