from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User

class UserRepository:
    @staticmethod
    def create(db: Session, username: str, email: str, hashed_password: str):
        
        db_user = User(
            username=username,
            email = email,
            hashed_password = hashed_password
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user
    
    @staticmethod
    def get_by_email(db: Session, email:str):
        toprint = select(User).where(User.email == email)
        
        res = db.execute(toprint)
        
        return res.scalar_one_or_none()