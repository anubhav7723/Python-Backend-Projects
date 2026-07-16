from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.schemas.user import UserCreate
from app.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return AuthService.create_user(db, user)