from fastapi import FastAPI
from app.schemas.task import TaskCreate

app = FastAPI()

print("Server Started")

@app.get("/")
def root():
    print("Inside Server")
    return {"message": "Welcome To Task Manager App"}

@app.post("/tasks")
def create_task(task: TaskCreate):
    return {
        "message": "Task Created successfully",
        "task" : task
    }