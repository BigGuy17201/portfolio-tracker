from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.database import engine
from backend import models
from backend.routers import holdings

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(holdings.router)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

