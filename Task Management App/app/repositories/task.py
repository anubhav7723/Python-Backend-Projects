from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.task import Task
from app.schemas.task import TaskCreate



class TaskRepository:
    @staticmethod
    def create(db: Session, task: TaskCreate):
        db_task = Task(
            title=task.title,
            description=task.description,
            priority=task.priority
        )

        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return db_task
    
    @staticmethod
    def get_all(db: Session):
        toprint = select(Task)
        res = db.execute(toprint)
        return res.scalars().all()
    
    @staticmethod
    def get_by_id(db: Session, task_id: int):
        toprint = select(Task).where(Task.id == task_id)
        
        res = db.execute(toprint)
        
        return res.scalar_one_or_none()
    
    @staticmethod
    def update(db: Session, task_id: int, task_data: TaskCreate):
        task = TaskRepository.get_by_id(db, task_id)
        
        if task is None:
            return None
        
        task.title = task_data.title
        task.description = task_data.description
        task.priority = task_data.priority
        
        db.commit()
        db.refresh(task)
        
        return task
    
    @staticmethod
    def delete(db: Session, task_id:int):
        task = TaskRepository.get_by_id(db, task_id)
        
        if task is None:
            return None
        
        db.delete(task)
        db.commit()
        
        return {"message": f"Task with id {task_id} deleted successfully"}