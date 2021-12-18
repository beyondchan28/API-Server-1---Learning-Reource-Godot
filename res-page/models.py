from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Resource(Base):
    __tablename__ = 'resources'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    source = Column(String)
    author = Column(String)
    genre = Column(String)
    year = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator = relationship("User", back_populates="resources")

class User(Base):
    __tablename__='users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    resources = relationship('Resource', back_populates="creator")
    