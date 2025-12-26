from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from typing import Union

class UserBase(SQLModel, table=True):
  id: Union[int, None] = Field(default=None, primary_key=True)
  first_name: str
  middle_name: str
  last_name: str
  email: EmailStr