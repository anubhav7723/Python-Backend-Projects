from sqlalchemy.orm import Session

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