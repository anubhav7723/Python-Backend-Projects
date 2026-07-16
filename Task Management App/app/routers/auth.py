from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.schemas.user import UserCreate
from app.schemas.user import UserLogin
from app.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.get("/")
def get_all_users(
    db: Session = Depends(get_db)
):
    return AuthService.get_all_users(db)


@router.post("/register")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return AuthService.create_user(db, user)

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return AuthService.login(db, user)