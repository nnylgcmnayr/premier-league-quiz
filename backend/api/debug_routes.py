from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db, engine, Base
from backend.database.models import Player, Team, Leaderboard
import backend.utils.etl_pipeline as etl

router = APIRouter()

@router.get("/reset-database")
async def reset_database(db: Session = Depends(get_db)):
    """Reset database - USE WITH CAUTION! (Development only)"""
    try:
        # Drop external data tables and recreate
        Base.metadata.drop_all(bind=engine, tables=[Player.__table__, Team.__table__])
        Base.metadata.create_all(bind=engine, tables=[Player.__table__, Team.__table__])

        # Repopulate with sample data
        players_dict, teams_dict = etl.etl_data() # get from data layer

        added_player_count = 0
        for player_data in players_dict:
            player = Player(**player_data)
            db.add(player)
            added_player_count += 1

        added_team_count = 0
        for team_data in teams_dict:
            team = Team(**team_data)
            db.add(team)
            added_team_count += 1

        db.commit()

        return {
            "message": "Database data reset successfully",
            "players_added": added_player_count,
            "teams_added": added_team_count
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error resetting database: {str(e)}")

@router.get("/reset-scores")
async def reset_database(db: Session = Depends(get_db)):
    """Reset user scoring data - USE WITH CAUTION! (Development only)"""
    try:
        # Drop external data tables and recreate
        Base.metadata.drop_all(bind=engine, tables=[Leaderboard.__table__])
        Base.metadata.create_all(bind=engine, tables=[Leaderboard.__table__])

        return {
            "message": "Database scores leaderboard reset successfully"
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error resetting database: {str(e)}")


@router.get("/database-info")
async def database_info(db: Session = Depends(get_db)):
    """Get database information for debugging"""
    try:
        # table count
        player_count = db.query(Player).count()
        team_count = db.query(Team).count()

        return {
            "message": "Database details: ",
            "players_total": player_count,
            "teams_total": team_count
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting database info: {str(e)}")