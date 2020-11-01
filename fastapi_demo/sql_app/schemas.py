from typing import List, Optional

from pydantic import BaseModel


class IdeaBase(BaseModel):
    title: str
    description: Optional[str] = None


class IdeaCreate(IdeaBase):
    pass


class Idea(IdeaBase):
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
    ideas: List[Idea] = []

    class Config:
        orm_mode = True