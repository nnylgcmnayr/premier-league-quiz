import React from 'react';

const Leaderboard = ({ leaderboard }) => {
  if (!leaderboard || leaderboard.length === 0) {
    return (
      <div className="text-gray-500 italic">
        No scores yet. Be the first to play!
      </div>
    );
  }

  return (
    <div className="text-left">
      <h3 className="text-lg font-bold text-gray-800 mb-3 text-center">
        🏆 Top 10 Leaderboard
      </h3>
      <div className="max-h-64 overflow-y-auto">
        {leaderboard.map((entry, index) => (
          <div
            key={entry.id || index}
            className="flex justify-between items-center py-2 px-3 border-b hover:bg-gray-50"
          >
            <span className="font-medium">
              #{entry.rank || index + 1} {entry.player_name}
            </span>
            <span className="text-blue-600 font-bold">
              {entry.score} pts
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Leaderboard;