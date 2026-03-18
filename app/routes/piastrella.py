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
    "The tiles are currently resting.",
    "Buy a new house, I will give you advice!",
    "You should update to dotnet 9, I'll help you, I am a Piastrella!",
    "Piastrella reminds you to smile and eat Tangerines",
    "Piastrella knows where you are and is coming to get you. To give you a smile!",
    "Are you operative? Piastrella is waiting!",
    "No space in the office for you? Just go back home and look at me, your Piastrella!"
]


@router.get("/")
def get_piastrella():
    return {"message": choice(messages)}