import React from 'react';
import { Trophy, Play } from 'lucide-react';
import Leaderboard from './Leaderboard';

const MenuScreen = ({ onStartGame, leaderboard }) => {
  return (
    <div className="min-h-screen flex items-center justify-center p-4 sm:p-6 md:p-8">
      <div className="bg-white rounded-xl shadow-2xl p-6 sm:p-8 max-w-md w-full text-center">
        <Trophy className="mx-auto text-yellow-500 w-12 h-12 sm:w-16 sm:h-16 mb-4" />

        <h1 className="text-3xl sm:text-4xl font-bold text-gray-800 mb-2">
          Premier League Quiz
        </h1>

        <p className="text-sm sm:text-base text-gray-600 mb-6">
          Match players to their teams. 45 seconds. +5 for correct, -5 for wrong!
        </p>

        <button
          onClick={onStartGame}
          className="bg-green-500 hover:bg-green-600 text-white font-bold py-3 sm:py-4 px-6 sm:px-8 rounded-lg text-lg sm:text-xl transition-colors mb-6 flex items-center justify-center mx-auto focus:outline-none focus:ring-4 focus:ring-green-300 w-full sm:w-auto"
          aria-label="Start Premier League Quiz Game"
        >
          <Play className="mr-2 w-5 h-5 sm:w-6 sm:h-6" aria-hidden="true" />
          Start Game
        </button>

        <Leaderboard leaderboard={leaderboard} />
      </div>
    </div>
  );
};

export default MenuScreen;