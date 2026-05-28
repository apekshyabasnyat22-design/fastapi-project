from fastapi import FastAPI, Depends
from teacher.router import router as teacher_router
from student.router import router as student_router
import uvicorn
from databases import engine, Base, get_db
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(teacher_router)
app.include_router(student_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}


# 3. Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)
