from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.repositories.user import UserRepository
from app.schemas.user import UserLogin

from app.core.security import hash_password, verify_password, create_access_token

class AuthService:
    @staticmethod
    def get_all_users(db: Session):
        return UserRepository.get_all_users(db)
    
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
    
    @staticmethod
    def login(db: Session, user: UserLogin):
        db_user = UserRepository.get_by_email(db, user.email)
        
        if db_user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or Password"
            )
        
        if not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password"
            )
            
        token = create_access_token({
            "sub": db_user.email
        })
        
        return {
            "access token" : token,
            "token_type": "bearer"
        }