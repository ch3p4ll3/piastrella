from fastapi import FastAPI
from pydantic import BaseModel

from app.routes import piastrella

app = FastAPI()

app.include_router(piastrella.router, prefix="/piastrella")
