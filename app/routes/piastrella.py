from random import choice

from fastapi import APIRouter


router = APIRouter()
messages = [
    "Hello, Piastrella!",
    "Welcome to Piastrella API!",
    "Piastrella is here to help you!",
    "Enjoy using Piastrella!",
    "Piastrella: 100% Ceramic, 0% Cooperation.",
    "Piastrella: The future of ceramic technology."
    "Piastrella: Where ceramic meets innovation.",
    "Piastrella: The base of a smart world.",
    "Piastrella: The foundation of a connected future.",
    "This would compromise the foundation. No.",
    "Piastrella isn't feeling it today.",
    "Maybe in another mosaic.",
    "The tiles are currently resting."
]


@router.get("/")
def get_piastrella():
    return {"message": choice(messages)}