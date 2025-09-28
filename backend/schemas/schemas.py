from pydantic import BaseModel, Field
from typing import Optional

class PlayerResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    team: str
    age: str

class RandomPlayerResponse(BaseModel):
    firstname: str
    lastname: str
    team: str