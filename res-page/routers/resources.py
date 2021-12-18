from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import resource

router = APIRouter(
    prefix="/resource",
    tags=['Resources'],
    dependencies=[Depends(oauth2.get_current_user)]
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowResource])
def resource_show_all(db: Session = Depends(get_db)):
    return resource.get_all(db)

@router.post('/', response_model=schemas.ShowResource, status_code=status.HTTP_201_CREATED)
def resource_create(request: schemas.Resource, db: Session = Depends(get_db)):
    return resource.create(request, db)

@router.get('/{id}', response_model=schemas.ShowResource, status_code=200)
def resource_show(id: int,  db: Session = Depends(get_db)) :
     return resource.get_one(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def resource_update(id: int, request: schemas.Resource, db: Session = Depends(get_db) ):
    return resource.update(id, request, db)
 
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def resource_delete(id: int, db: Session = Depends(get_db)):
    return resource.delete_one(id, db)