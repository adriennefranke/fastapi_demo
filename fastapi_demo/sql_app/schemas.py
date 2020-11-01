from typing import List, Optional

from pydantic import BaseModel


class itemBase(BaseModel):
    title: str
    description: Optional[str] = None


class itemCreate(itemBase):
    pass


class item(itemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[item] = []

    class Config:
        orm_mode = True