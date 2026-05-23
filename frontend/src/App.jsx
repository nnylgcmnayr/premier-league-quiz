import React, { useState, useEffect, useCallback } from 'react';
import './App.css';
import MenuScreen from './components/MenuScreen';
import GameScreen from './components/GameScreen';
import GameOverScreen from './components/GameOverScreen';
import { GAME_STATES } from './utils/constants';
import { apiService } from './services/api';

function App() {
  const [gameState, setGameState] = useState(GAME_STATES.MENU);
  const [score, setScore] = useState(0);
  const [gameStats, setGameStats] = useState({ correctAnswers: 0, wrongAnswers: 0, totalQuestions: 0 });
  const [leaderboard, setLeaderboard] = useState([]);

  // Load leaderboard on mount
  useEffect(() => {
    loadLeaderboard();
  }, []);

  const loadLeaderboard = useCallback(async () => {
    try {
      const data = await apiService.getLeaderboard();
      setLeaderboard(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error loading leaderboard:', error);
      setLeaderboard([]);
    }
  }, []);

  const startGame = useCallback(() => {
    setScore(0);
    setGameStats({ correctAnswers: 0, wrongAnswers: 0, totalQuestions: 0 });
    setGameState(GAME_STATES.PLAYING);
  }, []);

  const endGame = useCallback(async (finalScore, correctAnswers, wrongAnswers, totalQuestions) => {
    setScore(finalScore);
    setGameStats({ correctAnswers, wrongAnswers, totalQuestions });
    await loadLeaderboard();
    setGameState(GAME_STATES.FINISHED);
  }, [loadLeaderboard]);

  const returnToMenu = useCallback(async () => {
    await loadLeaderboard();
    setGameState(GAME_STATES.MENU);
  }, [loadLeaderboard]);

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
          gameStats={gameStats}
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