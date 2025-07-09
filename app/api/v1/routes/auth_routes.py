from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.schema.auth_schema import UserCreate, UserLogin
from app.services.auth_services import register_user, login_user

from app.core.config import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)