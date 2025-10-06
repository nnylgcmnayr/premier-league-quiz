from pydantic import BaseModel, Field
from datetime import datetime
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

class ScoreSubmission(BaseModel):
    player_name: str = Field(..., min_length=1, max_length=50)
    score: int
    game_duration: Optional[int] = None

class LeaderboardEntry(BaseModel):
    id: int
    player_name: str
    score: int
    timestamp: datetime
    rank: int