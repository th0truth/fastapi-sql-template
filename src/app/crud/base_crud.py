from typing import TypeVar, Union
from sqlmodel import SQLModel
from sqlalchemy import exc

from api.dependencies import AsyncSessionDep

ModelType = TypeVar("ModelType", bound=SQLModel)

class CRUDBase:
  def __init__(self, session: AsyncSessionDep, model: Union[ModelType, None] = None):
    self.session = session
    self.model = model

  async def create(
    self, obj: type[ModelType]
  ) -> Union[ModelType, None]:
    if self.model:
      obj = self.model.model_validate(obj)
    try:
      self.session.add(obj)
      await self.session.commit()
    except exc.IntegrityError:
      await self.session.rollback()
      return
    await self.session.refresh(obj)
    return obj
