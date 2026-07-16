from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.repositories.user import UserRepository

from app.core.security import hash_password

class AuthService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        existing_user = UserRepository.get_by_email(db, user.email)
        
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
            
        hashed_password = hash_password(user.password)
        
        return UserRepository.create(db, user.username, user.email, hashed_password)