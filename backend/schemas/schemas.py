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

class TeamResponse(BaseModel):
    id: int
    name: str
    points: int
    table_position: str
    wins: int
    loses: int
    draws: int