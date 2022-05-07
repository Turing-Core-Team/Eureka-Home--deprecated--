from fastapi import FastAPI
from src.app.routers.opportunities import opportunities_router

app = FastAPI()

app.include_router(opportunities_router)