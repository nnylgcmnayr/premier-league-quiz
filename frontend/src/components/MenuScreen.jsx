import React from 'react';
import { Trophy, Play } from 'lucide-react';
import Leaderboard from './Leaderboard';

const MenuScreen = ({ onStartGame, leaderboard }) => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 to-blue-600 flex items-center justify-center p-4">
      <div className="bg-white rounded-xl shadow-2xl p-8 max-w-md w-full text-center">
        <Trophy className="mx-auto text-yellow-500 w-16 h-16 mb-4" />

        <h1 className="text-4xl font-bold text-gray-800 mb-2">
          Premier League Quiz
        </h1>

        <p className="text-gray-600 mb-6">
          Match players to their teams. 10 seconds. +5 for correct, -5 for wrong!
        </p>

        <button
          onClick={onStartGame}
          className="bg-green-500 hover:bg-green-600 text-white font-bold py-4 px-8 rounded-lg text-xl transition-colors mb-6 flex items-center justify-center mx-auto"
        >
          <Play className="mr-2 w-6 h-6" />
          Start Game
        </button>

        <Leaderboard leaderboard={leaderboard} />
      </div>
    </div>
  );
};

export default MenuScreen;