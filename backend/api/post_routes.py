from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from google.cloud import pubsub_v1
import json
import os
from datetime import datetime, timezone

from backend.database.database import get_db
from backend.database.models import Leaderboard
from backend.schemas.schemas import ScoreSubmission

router = APIRouter()

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "premier-league-quiz-496917")
TOPIC_ID = os.getenv("PUBSUB_TOPIC_ID", "score-submitted")
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)


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

        # Publish to Pub/Sub
        message_data = {
            "player_name": score_data.player_name.strip(),
            "score": score_data.score,
            "game_duration": score_data.game_duration,
            "correct_answers": score_data.correct_answers,
            "wrong_answers": score_data.wrong_answers,
            "total_questions": score_data.total_questions,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "scenario": "cloud_run"
        }
        message_bytes = json.dumps(message_data).encode("utf-8")
        if os.getenv("K_SERVICE"):
            publisher.publish(topic_path, message_bytes)
        else:
            print(f"Local dev — Pub/Sub skipped for {score_data.player_name}")

        return {
            "message": "Score submitted successfully",
            "id": new_entry.id,
            "score": new_entry.score,
            "correct_answers": score_data.correct_answers,
            "wrong_answers": score_data.wrong_answers,
            "total_questions": score_data.total_questions
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error submitting score: {str(e)}")