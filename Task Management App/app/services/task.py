from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate
from app.repositories.task import TaskRepository


class TaskService:

    @staticmethod
    def create_task(db: Session, task: TaskCreate):
        return TaskRepository.create(db, task)
    
    @staticmethod
    def get_all_tasks(db: Session):
        return TaskRepository.get_all(db)
    
    @staticmethod
    def get_task_by_id(db:Session, task_id: int):
        return TaskRepository.get_by_id(db, task_id)
    
    @staticmethod
    def update_task(db: Session, task_id: int, task_data: TaskCreate):
        return TaskRepository.update(db, task_id, task_data)
    
    @staticmethod
    def delete_task(db: Session, task_id: int):
        return TaskRepository.delete(db, task_id)
    