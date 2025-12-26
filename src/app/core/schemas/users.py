from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from datetime import datetime
from typing import Union

class UserBase(SQLModel):
  first_name: str
  middle_name: str
  last_name: str
  email: EmailStr
  
class User(UserBase, table=True):
  id: Union[int, None] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
  password: str
  account_date: datetime