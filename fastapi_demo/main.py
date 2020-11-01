from typing import Optional, List

from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

class item(BaseModel):
    item_id: int
    item_name: str
    item_description: Optional[str] = None
    item_detail: Optional[str] = None
    item_creation_date: str
    user: str

class User(BaseModel):
    username: str
    email: Optional[str] = None

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/")
async def create_item(items: item):
    return item

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: item):
    return {"item_id": item_id, **item.dict()}

@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results