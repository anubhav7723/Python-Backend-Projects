from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate
from app.repositories.task import TaskRepository


class TaskService:

    @staticmethod
    def create_task(db: Session, task: TaskCreate):

        return TaskRepository.create(db, task)