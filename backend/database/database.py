from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from pathlib import Path

# Get the backend directory path
BACKEND_DIR = Path(__file__).parent.parent
DB_PATH = BACKEND_DIR / "premier_league_quiz.db"

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")

# For PostgreSQL, use: "postgresql://user:password@localhost/dbname"
# For development SQLite: "sqlite:///./premier_league_quiz.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()