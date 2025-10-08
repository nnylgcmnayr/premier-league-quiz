import React from 'react';

const TeamSelector = ({ teams, onTeamSelect, disabled }) => {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
      {teams.map((team) => (
        <button
          key={team.team_id || team}
          onClick={() => onTeamSelect(team.team_name || team)}
          disabled={disabled}
          className={`p-3 rounded-lg font-medium transition-all ${
            disabled
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-white hover:bg-blue-50 text-gray-800 shadow-md hover:shadow-lg'
          }`}
        >
          {team.team_name || team}
        </button>
      ))}
    </div>
  );
};

export default TeamSelector;