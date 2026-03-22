from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
items = [{"id": 1, "title": "Ship the first vertical slice"}]


class ItemIn(BaseModel):
    title: str


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/api/items")
def list_items():
    return items


@app.post("/api/items")
def create_item(payload: ItemIn):
    item = {"id": len(items) + 1, "title": payload.title}
    items.append(item)
    return item
