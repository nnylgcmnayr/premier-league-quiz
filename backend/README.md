# Backend - Premier League Quiz API

FastAPI backend providing RESTful API endpoints for the Premier League Quiz application.

## 🛠️ Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **PostgreSQL** - Relational database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## 📁 Project Structure

```
backend/
├── api/
│   ├── get_routes.py      # GET endpoints (players, teams, leaderboard)
│   ├── post_routes.py     # POST endpoints (submit score)
│   └── debug_routes.py    # Debug/testing endpoints
├── database/
│   ├── database.py        # Database connection
│   ├── models.py          # SQLAlchemy models
│   └── schemas.py         # Pydantic schemas
├── utils/
│   └── etl_pipeline.py    # ETL for loading player data
├── main.py                # Application entry point
└── requirements.txt       # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 14+

### Installation

1. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

4. **Run the server**
   ```bash
   python -m backend.main
   ```

   Server will be available at `http://localhost:8000`

## 📊 API Endpoints

### Player Endpoints
- `GET /api/players/random` - Get random player for quiz
  ```json
  {
    "player_id": 123,
    "firstname": "Harry",
    "lastname": "Kane",
    "age": "30",
    "team_name": "Bayern Munich"
  }
  ```

### Team Endpoints
- `GET /api/teams` - Get all teams
  ```json
  [
    {"team_id": 1, "team_name": "Arsenal"},
    {"team_id": 2, "team_name": "Chelsea"}
  ]
  ```

### Leaderboard Endpoints
- `GET /api/leaderboard` - Get top 10 scores (ranked)
- `POST /api/leaderboard` - Submit new score
  ```json
  {
    "player_name": "John",
    "score": 25
  }
  ```

### Debug Endpoints
- `GET /api/debug/players` - View all players
- `GET /api/debug/leaderboard` - View full leaderboard

## 🗃️ Database Schema

### Players Table
```sql
CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    age VARCHAR(10),
    team_name VARCHAR(100)
);
```

### Teams Table
```sql
CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) UNIQUE
);
```

### Leaderboard Table
```sql
CREATE TABLE leaderboard (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(100),
    score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔧 Configuration

### Environment Variables
- `DATABASE_URL` - PostgreSQL connection string
- `ALLOWED_ORIGINS` - Comma-separated CORS origins

### CORS Configuration
Configured to accept requests from:
- Development: `http://localhost:3000`
- Production: Set via `ALLOWED_ORIGINS` env var

## 🚀 Deployment (Railway)

1. Push code to GitHub
2. Connect repository to Railway
3. Add environment variables in Railway dashboard
4. Railway will auto-detect and deploy using Procfile

## 📝 Development Notes

- Database tables are created automatically on startup
- ETL pipeline runs once to populate player data
- Uses async context manager for database lifecycle
