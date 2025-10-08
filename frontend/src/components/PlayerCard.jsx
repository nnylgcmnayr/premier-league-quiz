import React from 'react';

const PlayerCard = ({ player, feedback }) => {
  return (
    <div className="bg-white rounded-xl shadow-2xl p-8 mb-6 text-center">
      <h2 className="text-4xl font-bold text-gray-800 mb-6">
        {player.firstname} {player.lastname}
      </h2>

      <p className="text-xl text-gray-600 mb-8">
        Which team does this player play for?
      </p>

      {feedback && (
        <div className={`text-xl font-bold mb-6 p-4 rounded-lg ${
          feedback.includes('✅') 
            ? 'bg-green-100 text-green-800' 
            : 'bg-red-100 text-red-800'
        }`}>
          {feedback}
        </div>
      )}
    </div>
  );
};

export default PlayerCard;