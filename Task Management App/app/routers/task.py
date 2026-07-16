from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.schemas.task import TaskCreate
from app.services.task import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return TaskService.create_task(db, task)


@router.get("/")
def get_all_tasks(
    db: Session = Depends(get_db)
):
    return TaskService.get_all_tasks(db)

@router.get("/{task_id}")
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = TaskService.get_task_by_id(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not Found"
        )
    
    return task

@router.put("/{task_id}")
def update_task(
    task_id:int,
    task_data:TaskCreate,
    db: Session = Depends(get_db)
):
    updated_task = TaskService.update_task(db, task_id, task_data)
    
    if updated_task is None:
        raise HTTPException(
            status_code=404, 
            detail="Task not Found"
        )
        
    return updated_task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    deleted = TaskService.delete_task(db, task_id)
    
    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Task not Found"
        )
        
    return deleted