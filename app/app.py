from fastapi import FastAPI

app = FastAPI()

items = ["Docker", "FastAPI", "Python"]


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


@app.post("/items/{name}")
def add_item(name: str):
    items.append(name)
    return {"message": f"{name} added", "items": items}