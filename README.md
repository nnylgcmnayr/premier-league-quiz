# Premier League Quiz 🏆⚽

A full-stack web application that tests users' knowledge of Premier League players through an interactive timed quiz game with real-time leaderboards.

Play here: https://prem-league-quiz.netlify.app/

## 🎯 Features

- **Timed Gameplay**: 60-second rounds testing player-to-team knowledge
- **Dynamic Scoring**: +5 points for correct answers, -5 for incorrect
- **Real-time Leaderboard**: Persistent top-10 rankings with live updates
- **Responsive Design**: Mobile-first UI built with Tailwind CSS
- **5000+ Player Database**: Comprehensive Premier League player data via ETL pipeline

## 🛠️ Tech Stack

### Frontend
- **React** - Component-based UI with hooks (useState, useEffect)
- **Tailwind CSS** - Utility-first responsive styling
- **Lucide React** - Modern icon library
- **Axios** - HTTP client for API communication

### Backend
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Relational database for player data and scores
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation and type safety
- **Uvicorn** - ASGI server

### DevOps & Tools
- **Railway** - Backend hosting (planned)
- **Netlify** - Frontend hosting (planned)
- **Git** - Version control

## 📁 Project Structure

```
prem_league_web_app/
├── backend/              # FastAPI backend
│   ├── api/             # API route handlers
│   ├── database/        # Models and database config
│   ├── utils/           # ETL pipeline and utilities
│   └── main.py          # Application entry point
├── frontend/            # React frontend
│   ├── public/          # Static assets
│   └── src/
│       ├── components/  # React components
│       ├── services/    # API client
│       └── utils/       # Constants and helpers
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+

### Backend Setup

1. **Navigate to project root**
   ```bash
   cd prem_league_web_app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   # Create .env file in root with:
   DATABASE_URL=postgresql://user:password@localhost/prem_league_quiz
   ```

5. **Run backend server**
   ```bash
   python -m backend.main
   ```
   Server runs on `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set environment variables**
   ```bash
   # Create .env file in frontend/ with:
   REACT_APP_API_URL=http://localhost:8000
   ```

4. **Run development server**
   ```bash
   npm start
   ```
   App runs on `http://localhost:3000`

## 📊 API Endpoints

### GET Endpoints
- `GET /api/players/random` - Get random player for quiz
- `GET /api/teams` - Get all Premier League teams
- `GET /api/leaderboard` - Get top 10 scores

### POST Endpoints
- `POST /api/leaderboard` - Submit new score
  ```json
  {
    "player_name": "string",
    "score": 0
  }
  ```

### Debug Endpoints
- `GET /api/debug/players` - View all players
- `GET /api/debug/leaderboard` - View full leaderboard

## 🏗️ Architecture Highlights

### ETL Pipeline
- Extracts 5000+ player records from RapidAPI
- Transforms data with Pandas
- Loads into PostgreSQL using SQLAlchemy ORM

### Database Schema
```sql
Players (player_id, firstname, lastname, age, team_name)
Teams (team_id, team_name)
Leaderboard (id, player_name, score, rank, created_at)
```

### Ranked Leaderboard Query
Uses SQL window functions for efficient ranking:
```sql
SELECT *,
       RANK() OVER (ORDER BY score DESC) as rank
FROM leaderboard
WHERE rank <= 10
```

## 🎨 Design Features

- **Accessibility**: ARIA labels, screen reader support, keyboard navigation
- **Responsive Breakpoints**: Mobile, tablet, and desktop optimized
- **Color-coded Timer**: Visual urgency indicators (blue → orange → red)
- **Medal System**: 🥇🥈🥉 for top 3 leaderboard positions

## 📝 Future Enhancements

- [ ] User authentication and profiles
- [ ] Multiple difficulty levels
- [ ] Statistics tracking (accuracy, streaks)
- [ ] Share scores on social media
- [ ] Dark mode support
- [ ] Multiplayer mode

## 👤 Author

**Ryan McGlynn**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 📄 License

This project is for educational/portfolio purposes. Player data sourced from public APIs.

## 🙏 Acknowledgments

- Premier League player data from RapidAPI
- Icons from Lucide React
- Inspired by football quiz games
