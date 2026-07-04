from fastapi import FastAPI
from app.schemas.task import TaskCreate
from fastapi import HTTPException


app = FastAPI()

temp_memo = []
task_id = 1

@app.get("/")
def root():
    print("Inside Server")
    return {"message": "Welcome To Task Manager App"}

#To add task in temp_memo
@app.post("/tasks")
def create_task(task: TaskCreate):
    global task_id
    
    new_task = {
        "id" : task_id,
        "title" : task.title,
        "description": task.description,
        "priority": task.priority
    }
    
    temp_memo.append(new_task)
    task_id += 1
     
    return new_task
    
#To see all tasks that are stored in temp_memo
@app.get("/tasks")
def get_task():
    return temp_memo

#to see particular task with id 
@app.get("/tasks/{call_id}")
def get_task_with_id(call_id : int):
    for task in temp_memo:
        if task["id"] == call_id:
            return task
        
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
        
#To update particular task
@app.put("/tasks/{call_id}")
def update_task(call_id : int, new_message :TaskCreate):
    for task in temp_memo:
        if task["id"] == call_id:
            task.update(new_message.model_dump())
            return task
        
    raise HTTPException(
        status_code=404, 
        detail="Task Not Found"
    )
    
#To delete particular task from list(temp_memo)
@app.delete("/tasks/{call_id}")
def remove_task(call_id : int):
    for task in temp_memo:
        if task["id"] == call_id:
            temp_memo.remove(task)
            
            return {"message": "Successfully Removed"}
        
    raise HTTPException(
        status_code=404, 
        detail="Task not found"
    )