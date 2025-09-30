from fastapi import FastAPI
from contextlib import asynccontextmanager

from database.database import engine, SessionLocal
from database.models import Base, Player, Team
from api import get_routes, debug_routes
import utils.etl_pipeline as etl

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up Premier League Quiz API...")

    # Create tables
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {e}")

    # Initialize database with data
    db = SessionLocal()
    try:
        # Check if players table exists and is empty
        player_count = db.query(Player).count()
        teams_count = db.query(Team).count()
        players_dict = None
        teams_dict = None
        if player_count == 0 or teams_count == 0:
            players_dict, teams_dict = etl.etl_data()
        if player_count == 0:
            print("Populating database with sample players...")
            for player_data in players_dict:
                player = Player(**player_data)
                db.add(player)
            db.commit()
            print(f"Successfully added {len(players_dict)} players to database")
        else:
            print(f"Database already contains {player_count} player")
        if teams_count == 0:
            print("Populating database with sample teams...")
            for team_data in teams_dict:
                team = Team(**team_data)
                db.add(team)
            db.commit()
            print(f"Successfully added {len(teams_dict)} teams to database")
        else:
            print(f"Database already contains {teams_count} teams")
    except Exception as e:
        print(f"Error populating database: {e}")
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

# Include routers with prefixes
app.include_router(get_routes.router, prefix="/api", tags=["GET Endpoints"])
# app.include_router(post_routes.router, prefix="/api", tags=["POST Endpoints"])
app.include_router(debug_routes.router, prefix="/api/debug", tags=["Debug Endpoints"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)