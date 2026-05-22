from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from backend.database.database import engine, SessionLocal
from backend.database.models import Base, Player, Team, Leaderboard
from backend.api import get_routes, debug_routes, post_routes
import backend.utils.etl_pipeline as etl

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up Premier League Quiz API...")

    # Create tables
    try:
        # Create all imported models
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {e}")

    # Sync database with latest FPL data on every startup.
    # Previously this only ran when the DB was empty — now it runs every time
    # so that player transfers, team changes, and can_select status stay current.
    db = SessionLocal()
    try:
        print("Syncing database with FPL API...")
        players_dict, teams_dict = etl.etl_data()

        # db.merge() upserts: inserts if the primary key is new, updates if it already exists.
        # Players with can_select=False are excluded upstream in the ETL pipeline.
        for player_data in players_dict:
            db.merge(Player(**player_data))

        # Remove any players no longer present in the latest FPL data
        # (e.g. departed players, or those newly marked can_select=False)
        current_player_ids = {p['player_id'] for p in players_dict}
        db.query(Player).filter(Player.player_id.notin_(current_player_ids)).delete(synchronize_session=False)
        db.commit()
        print(f"Synced {len(players_dict)} players")

        for team_data in teams_dict:
            db.merge(Team(**team_data))

        # Remove any teams no longer present in the latest FPL data
        current_team_ids = {t['team_id'] for t in teams_dict}
        db.query(Team).filter(Team.team_id.notin_(current_team_ids)).delete(synchronize_session=False)
        db.commit()
        print(f"Synced {len(teams_dict)} teams")

    except Exception as e:
        print(f"Error syncing database: {e}")
        db.rollback()
    finally:
        db.close()

    yield  # This is where the app runs

    # Shutdown
    print("Shutting down Premier League Quiz API...")


# FastAPI app with lifespan handler
app = FastAPI(
    title="Premier League Quiz API",
    description="API for Premier League player quiz game",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
import os
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Will be set via environment variable in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with prefixes
app.include_router(get_routes.router, prefix="/api", tags=["GET Endpoints"])
app.include_router(post_routes.router, prefix="/api", tags=["POST Endpoints"])
app.include_router(debug_routes.router, prefix="/api/debug", tags=["Debug Endpoints"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)