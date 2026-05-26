import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/project1/v1/")
def root():
    return {"message": "Hello World, welcome to FastAPI!"}

@app.get("/test")
def test():
    return {"message": "Hello world, test!"}

@app.get("/home")
def home():
    return {"message": "Welcome to the home page!"}


# Request body model
class NumberRequest(BaseModel):
    number: int


@app.post("/home")
def add_number(data: NumberRequest):
    return {"number": data.number}

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI root!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # FastAPI automatically converts item_id to an integer because of the type hint!
    return {"item_id": item_id, "type": type(item_id)}

print("Route /items/{item_id} added.")

@app.post("/items/{item_id}")
async def read_item(item_id: int):
    # FastAPI automatically converts item_id to an integer because of the type hint!
    return {"item_id": item_id, "type": type(item_id)}

print("Route /items/{item_id} added.")

@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    return {
        "skip": skip.name,
        "limit": limit,
        "data": ["user1", "user2", "user3"][skip : skip + limit]
    }

print("Route /users/ added.")

@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "data": ["user1", "user2", "user3"][skip : skip + limit]
    }

print("Route /users/ added.")

if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)