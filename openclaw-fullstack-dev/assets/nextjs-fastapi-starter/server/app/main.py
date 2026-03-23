from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3100",
        "http://127.0.0.1:3100",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
