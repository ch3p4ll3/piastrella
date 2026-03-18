from os import getenv

from fastapi import FastAPI

from app.routes import piastrella


app = FastAPI()
env = getenv("ENV", "development")

if env == "docker":
    title = "Piastrella API (Docker) - Jonatan loves Docker"
    print(title)
    app.title = title

app.include_router(piastrella.router, prefix="/piastrella")
