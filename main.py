from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", lt=10), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results