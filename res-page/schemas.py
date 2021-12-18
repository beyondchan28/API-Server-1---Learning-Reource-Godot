from typing import List, Optional
from pydantic import BaseModel

class ResourceBase(BaseModel):
    title: str
    source: str
    author: str
    genre: str
    year: int

class Resource (ResourceBase):
    class Config():
        orm_mode= True

class User(BaseModel):
    name: str
    email: str
    password: str
    

class ShowUser(BaseModel):
    name: str
    email: str
    resources: List[Resource]
    class Config():
        orm_mode= True
        

class UserForResource(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode= True

class ShowResource(BaseModel):
    title: str
    source: str
    author: str
    genre: str
    year: int
    creator: UserForResource
    
    class Config():
        orm_mode= True

class Login(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    email: Optional[str] = None