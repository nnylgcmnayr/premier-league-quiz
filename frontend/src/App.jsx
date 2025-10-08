import React, { useState, useEffect } from 'react';
import './App.css';
import MenuScreen from './components/MenuScreen';
import GameScreen from './components/GameScreen';
import GameOverScreen from './components/GameOverScreen';
import { GAME_STATES } from './utils/constants';
import { apiService } from './services/api';

function App() {
  const [gameState, setGameState] = useState(GAME_STATES.MENU);
  const [score, setScore] = useState(0);
  const [leaderboard, setLeaderboard] = useState([]);

  // Load leaderboard on mount
  useEffect(() => {
    loadLeaderboard();
  }, []);

  const loadLeaderboard = async () => {
    try {
      const data = await apiService.getLeaderboard();
      setLeaderboard(data);
    } catch (error) {
      console.error('Error loading leaderboard:', error);
    }
  };

  const startGame = () => {
    setScore(0);
    setGameState(GAME_STATES.PLAYING);
  };

  const endGame = async (finalScore) => {
    setScore(finalScore);
    await loadLeaderboard(); // Refresh leaderboard when game ends
    setGameState(GAME_STATES.FINISHED);
  };

  const returnToMenu = async () => {
    await loadLeaderboard(); // Refresh leaderboard
    setGameState(GAME_STATES.MENU);
  };

  return (
    <div className="App">
      {gameState === GAME_STATES.MENU && (
        <MenuScreen
          onStartGame={startGame}
          leaderboard={leaderboard}
        />
      )}

      {gameState === GAME_STATES.PLAYING && (
        <GameScreen
          onGameEnd={endGame}
        />
      )}

      {gameState === GAME_STATES.FINISHED && (
        <GameOverScreen
          score={score}
          leaderboard={leaderboard}
          onReturnToMenu={returnToMenu}
          onPlayAgain={startGame}
          onScoreSubmitted={loadLeaderboard}
        />
      )}
    </div>
  );
}

export default App;