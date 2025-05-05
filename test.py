from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/search/")
def search_items(query: str):
    return {"query": "This is the query part"}
