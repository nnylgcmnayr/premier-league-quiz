# Frontend - Premier League Quiz

React-based frontend for the Premier League Quiz application featuring responsive design and real-time gameplay.

## 🛠️ Tech Stack

- **React** - UI library with hooks
- **Tailwind CSS** - Utility-first styling
- **Lucide React** - Icon library
- **Axios** - HTTP client

## 📁 Component Structure

```
src/
├── components/
│   ├── MenuScreen.jsx        # Landing page with leaderboard
│   ├── GameScreen.jsx         # Main quiz gameplay
│   ├── GameOverScreen.jsx     # End screen with score submission
│   ├── PlayerCard.jsx         # Player display card
│   ├── TeamSelector.jsx       # Team selection grid
│   └── Leaderboard.jsx        # Top 10 rankings display
├── services/
│   └── api.js                # API client (Axios)
├── utils/
│   └── constants.js          # Game config and states
├── App.jsx                   # Main app component
└── index.js                  # Entry point
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Backend API running (see `/backend/README.md`)

### Installation

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your backend URL
   ```

3. **Run development server**
   ```bash
   npm start
   ```

   App will be available at `http://localhost:3000`

### Build for Production

```bash
npm run build
```

Optimized production build will be in `build/` directory.

## 🎮 Game Flow

1. **Menu Screen** - View leaderboard and start game
2. **Game Screen** - 60-second quiz with player-to-team matching
3. **Game Over** - Submit score and view updated leaderboard

## 🎨 Features

### Responsive Design
- Mobile-first approach
- Breakpoints: `sm` (640px), `md` (768px), `lg` (1024px)
- Adaptive grid layouts (2/3/4/5 columns)

### Accessibility
- ARIA labels on interactive elements
- Live regions for screen readers
- Keyboard navigation support
- Focus states on all buttons

### Visual Enhancements
- Color-coded timer (blue → orange → red)
- Medal emojis for top 3 (🥇🥈🥉)
- Smooth transitions and animations
- Gradient backgrounds

## 📦 Key Dependencies

```json
{
  "react": "^18.2.0",
  "axios": "^1.5.0",
  "lucide-react": "^0.263.1",
  "tailwindcss": "^3.3.0"
}
```

## 🚀 Deployment (Netlify)

### Automatic Deployment
1. Push code to GitHub
2. Connect repository to Netlify
3. Netlify will use `netlify.toml` config
4. Set environment variable: `REACT_APP_API_URL`

### Manual Build
```bash
npm run build
# Upload build/ folder to Netlify
```

## 🔧 Configuration

### Environment Variables
- `REACT_APP_API_URL` - Backend API endpoint

### Game Constants
Located in `src/utils/constants.js`:
- `GAME_DURATION`: 45 seconds
- `CORRECT_POINTS`: +5
- `INCORRECT_POINTS`: -5

## 📝 Development Notes

- Uses React hooks (no class components)
- Tailwind CSS for all styling
- Axios interceptors for API error handling
- State management via useState/useEffect
