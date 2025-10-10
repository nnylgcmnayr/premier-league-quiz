import React from 'react';

const TeamSelector = ({ teams, onTeamSelect, disabled }) => {
  // Ensure teams is always an array
  const teamList = Array.isArray(teams) ? teams : [];

  return (
    <div
      className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3 md:gap-4"
      role="group"
      aria-label="Select team"
    >
      {teamList.map((team) => (
        <button
          key={team.team_id || team}
          onClick={() => onTeamSelect(team.team_name || team)}
          disabled={disabled}
          aria-label={`Select ${team.team_name || team}`}
          className={`p-3 md:p-4 rounded-lg font-medium transition-all duration-200 transform ${
            disabled
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed opacity-60'
              : 'bg-white hover:bg-blue-50 text-gray-800 shadow-md hover:shadow-xl hover:scale-105 active:scale-95 focus:outline-none focus:ring-4 focus:ring-blue-300'
          }`}
        >
          <span className="text-sm md:text-base font-semibold">
            {team.team_name || team}
          </span>
        </button>
      ))}
    </div>
  );
};

export default TeamSelector;