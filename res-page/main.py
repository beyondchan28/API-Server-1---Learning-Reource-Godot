from fastapi import FastAPI
from . import models
from .database import engine
from .routers import resources, user, authentication


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(resources.router)
app.include_router(user.router)


