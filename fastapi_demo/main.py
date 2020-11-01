from typing import Optional, List

from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

class Idea(BaseModel):
    idea_id: int
    idea_name: str
    idea_description: Optional[str] = None
    idea_detail: Optional[str] = None
    idea_creation_date: str
    user: str

class User(BaseModel):
    username: str
    email: Optional[str] = None

billow = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@billow.post("/ideas/")
async def create_item(ideas: Idea):
    return idea

@billow.put("/ideas/{idea_id}")
async def create_item(idea_id: int, idea: Idea):
    return {"idea_id": idea_id, **idea.dict()}

@billow.get("/ideas/")
async def read_ideas(q: Optional[str] = None):
    results = {"ideas": [{"idea_id": "Foo"}, {"idea_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results