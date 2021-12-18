from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import Integer
from fastapi import HTTPException,status
from .. import models, schemas


def get_all(db: Session):
    resources = db.query(models.Resource).all()
    return resources

def create(request: schemas.Resource, db: Session):
    new_resource = models.Resource(title=request.title , source=request.source, author=request.author, genre=request.genre, year=request.year, user_id=1) #user_id msh hard coded
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

def delete_one(id: Integer, db: Session):
    resource = db.query(models.Resource).filter(models.Resource.id == id)
    if not resource.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id {id} is not exist.")
    resource.delete(synchronize_session=False)
    db.commit()
    return "Data deleted successfully."

def update(id: Integer, request: schemas.Resource, db:Session):
    resource = db.query(models.Resource).filter(models.Resource.id == id)
    if not resource.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id {id} is not exist.")
    resource.update(request.dict())
    db.commit()
    return "Data updated successfully."

def get_one(id: Integer, db:Session):
    resource = db.query(models.Resource).filter(models.Resource.id == id).first()
    if not resource:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Resource with id {id} is not exist.")
    return resource