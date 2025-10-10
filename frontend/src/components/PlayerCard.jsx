import React from 'react';

const PlayerCard = ({ player, feedback }) => {
  return (
    <div className="bg-white rounded-xl shadow-2xl p-8 mb-6 text-center transform transition-all duration-300 hover:shadow-3xl">
      <div className="mb-6">
        <div className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-2">
          Player
        </div>
        <h2 className="text-4xl md:text-5xl font-bold text-gray-800 mb-2">
          {player.firstname} {player.lastname}
        </h2>
      </div>

      <div className="border-t border-gray-200 pt-6">
        <p className="text-xl md:text-2xl text-gray-600 font-medium">
          Which team does this player play for?
        </p>
      </div>

      {feedback && (
        <div
          role="status"
          aria-live="assertive"
          aria-atomic="true"
          className={`mt-6 text-lg md:text-xl font-bold p-4 rounded-lg transition-all duration-300 ${
            feedback.includes('✅')
              ? 'bg-green-100 text-green-800 border-2 border-green-300'
              : 'bg-red-100 text-red-800 border-2 border-red-300'
          }`}
        >
          {feedback}
        </div>
      )}
    </div>
  );
};

export default PlayerCard;