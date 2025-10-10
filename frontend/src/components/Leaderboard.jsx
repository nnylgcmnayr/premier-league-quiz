import React from 'react';

const getMedalEmoji = (rank) => {
  switch (rank) {
    case 1: return '🥇';
    case 2: return '🥈';
    case 3: return '🥉';
    default: return null;
  }
};

const Leaderboard = ({ leaderboard }) => {
  // Ensure leaderboard is always an array
  if (!leaderboard || !Array.isArray(leaderboard) || leaderboard.length === 0) {
    return (
      <div className="text-gray-500 italic py-4">
        No scores yet. Be the first to play!
      </div>
    );
  }

  return (
    <div className="text-left">
      <h3
        className="text-lg md:text-xl font-bold text-gray-800 mb-4 text-center"
        id="leaderboard-heading"
      >
        🏆 Top 10 Leaderboard
      </h3>
      <div
        className="max-h-80 overflow-y-auto rounded-lg border border-gray-200"
        role="list"
        aria-labelledby="leaderboard-heading"
      >
        {leaderboard.map((entry, index) => {
          const rank = entry.rank || index + 1;
          const medal = getMedalEmoji(rank);

          return (
            <div
              key={entry.id || index}
              role="listitem"
              aria-label={`Rank ${rank}: ${entry.player_name} with ${entry.score} points`}
              className={`flex justify-between items-center py-3 px-4 border-b last:border-b-0 transition-colors ${
                rank <= 3 ? 'bg-gradient-to-r from-yellow-50 to-white' : 'hover:bg-gray-50'
              }`}
            >
              <div className="flex items-center gap-3">
                <span className="font-bold text-gray-600 min-w-[2rem]" aria-hidden="true">
                  {medal || `#${rank}`}
                </span>
                <span className="font-medium text-gray-800">
                  {entry.player_name}
                </span>
              </div>
              <span className="text-blue-600 font-bold text-lg">
                {entry.score} pts
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Leaderboard;