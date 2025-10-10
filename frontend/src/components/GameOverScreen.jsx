import React, { useState, useEffect } from 'react';
import { Trophy, RotateCcw, Home } from 'lucide-react';
import { apiService } from '../services/api';
import Leaderboard from './Leaderboard';

const GameOverScreen = ({ score, leaderboard, onReturnToMenu, onPlayAgain, onScoreSubmitted }) => {
  const [playerName, setPlayerName] = useState('');
  const [showNameInput, setShowNameInput] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    console.log('GameOverScreen - leaderboard updated:', leaderboard);
  }, [leaderboard]);

  const handleSubmitScore = async () => {
    if (!playerName.trim()) return;

    try {
      setSubmitting(true);
      await apiService.submitScore(playerName, score);
      // Reload leaderboard BEFORE hiding the input
      if (onScoreSubmitted) {
        await onScoreSubmitted();
      }
      setShowNameInput(false);
      alert('Score submitted successfully!');
    } catch (error) {
      console.error('Error submitting score:', error);
      alert('Failed to submit score. Please try again.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="bg-white rounded-xl shadow-2xl p-8 max-w-md w-full text-center">
        <Trophy className="mx-auto text-yellow-500 w-16 h-16 mb-4" />

        <h1 className="text-3xl font-bold text-gray-800 mb-4">
          Time's Up!
        </h1>

        <p
          className="text-5xl font-bold text-blue-600 mb-6"
          role="status"
          aria-live="polite"
          aria-label={`You scored ${score} points`}
        >
          {score} points
        </p>

        {showNameInput ? (
          <div className="mb-6">
            <p className="text-gray-600 mb-4 text-lg">
              Enter your name for the leaderboard:
            </p>
            <input
              type="text"
              value={playerName}
              onChange={(e) => setPlayerName(e.target.value)}
              placeholder="Your name"
              maxLength={30}
              aria-label="Enter your name for the leaderboard"
              aria-required="true"
              className="w-full p-3 md:p-4 border-2 border-gray-300 rounded-lg mb-4 text-center text-lg
                focus:border-blue-500 focus:ring-4 focus:ring-blue-200 focus:outline-none
                transition-all duration-200 placeholder-gray-400"
              onKeyPress={(e) => e.key === 'Enter' && handleSubmitScore()}
              disabled={submitting}
              autoFocus
            />
            <button
              onClick={handleSubmitScore}
              disabled={submitting || !playerName.trim()}
              aria-label="Submit your score to the leaderboard"
              className="bg-blue-500 hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed
                text-white font-bold py-3 px-8 rounded-lg transition-all duration-200
                transform hover:scale-105 active:scale-95 focus:outline-none focus:ring-4 focus:ring-blue-300"
            >
              {submitting ? 'Submitting...' : 'Submit Score'}
            </button>
          </div>
        ) : (
          <div className="mb-6">
            <Leaderboard leaderboard={leaderboard} />
          </div>
        )}

        <div className="flex gap-4 justify-center">
          <button
            onClick={onPlayAgain}
            aria-label="Play game again"
            className="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-lg transition-colors flex items-center focus:outline-none focus:ring-4 focus:ring-green-300"
          >
            <RotateCcw className="mr-2 w-5 h-5" aria-hidden="true" />
            Play Again
          </button>

          <button
            onClick={onReturnToMenu}
            aria-label="Return to main menu"
            className="bg-gray-500 hover:bg-gray-600 text-white font-bold py-3 px-6 rounded-lg transition-colors flex items-center focus:outline-none focus:ring-4 focus:ring-gray-400"
          >
            <Home className="mr-2 w-5 h-5" aria-hidden="true" />
            Menu
          </button>
        </div>
      </div>
    </div>
  );
};

export default GameOverScreen;