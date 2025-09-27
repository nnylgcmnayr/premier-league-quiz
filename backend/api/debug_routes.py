from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db, engine, Base
from backend.database.models import Player
import backend.utils.etl_pipeline as etl

router = APIRouter()

@router.get("/reset-database")
async def reset_database(db: Session = Depends(get_db)):
    """Reset database - USE WITH CAUTION! (Development only)"""
    try:
        # Drop all tables and recreate
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        # Repopulate with sample data
        added_count = 0
        players_dict = etl.etl_data()
        for player_data in players_dict:
            player = Player(**player_data)
            db.add(player)
            added_count += 1

        db.commit()

        return {
            "message": "Database reset successfully",
            "players_added": added_count
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error resetting database: {str(e)}")


@router.get("/database-info")
async def database_info(db: Session = Depends(get_db)):
    """Get database information for debugging"""
    try:
        player_count = db.query(Player).count()

        # Get players
        players = db.query(Player).limit(5).all()

        return {
            "player_count": player_count,
            "sample_players": [
                {
                    "player_id": p.player_id,
                    "firstname": p.firstname,
                    "team_name": p.team_name,
                    "position": p.position,
                }
                for p in players
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting database info: {str(e)}")