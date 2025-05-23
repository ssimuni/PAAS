from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import User
from database import get_db

router = APIRouter()

@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}