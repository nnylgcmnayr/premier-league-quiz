from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session
from typing import List
import random

from backend.database.database import get_db
from backend.database.models import Player
from backend.schemas.schemas import RandomPlayerResponse, PlayerResponse

# API Routes

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Premier League Quiz API", "version": "1.0.0"}


@router.get("/random-player", response_model=RandomPlayerResponse)
async def get_random_player(db: Session = Depends(get_db)):
    """Get a random player for the quiz"""
    try:
        # Get total count of players
        total_players = db.query(Player).count()

        if total_players == 0:
            raise HTTPException(status_code=404, detail="No players found in database")

        # Get a random player
        random_offset = random.randint(0, total_players - 1)
        random_player = db.query(Player).offset(random_offset).first()

        return RandomPlayerResponse(
            firstname=random_player.firstname,
            lastname=random_player.lastname,
            team=random_player.team_name
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching random player: {str(e)}")

@router.get("/players", response_model=List[PlayerResponse])
async def get_all_players(db: Session = Depends(get_db)):
    """Get all players (for admin purposes)"""
    try:
        players = db.query(Player).all()
        return [
            PlayerResponse(
                id=player.player_id,
                firstname=player.firstname,
                lastname=player.lastname,
                team=player.team_name
            )
            for player in players
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching players: {str(e)}")
