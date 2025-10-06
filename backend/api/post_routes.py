from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.database.models import Leaderboard
from backend.schemas.schemas import ScoreSubmission

router = APIRouter()


@router.post("/scores", response_model=dict)
async def submit_score(score_data: ScoreSubmission, db: Session = Depends(get_db)):
    """Submit a new score to the leaderboard"""
    try:
        # Validate score (reasonable bounds)
        if score_data.score < -500 or score_data.score > 500:
            raise HTTPException(status_code=400, detail="Invalid score range")

        # Create new leaderboard entry
        new_entry = Leaderboard(
            player_name=score_data.player_name.strip(),
            score=score_data.score,
            game_duration=score_data.game_duration
        )

        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)

        return {
            "message": "Score submitted successfully",
            "id": new_entry.id,
            "score": new_entry.score
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error submitting score: {str(e)}")