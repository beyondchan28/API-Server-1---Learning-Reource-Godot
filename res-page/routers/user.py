from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from .. import database, schemas

from ..repository import user

from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User,  db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_one(id, db)