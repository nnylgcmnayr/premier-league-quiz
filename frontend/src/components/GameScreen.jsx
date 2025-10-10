import React, { useState, useEffect, useRef } from 'react';
import { Clock } from 'lucide-react';
import { apiService } from '../services/api';
import { GAME_CONFIG } from '../utils/constants';
import PlayerCard from './PlayerCard';
import TeamSelector from './TeamSelector';

const GameScreen = ({ onGameEnd }) => {
  const [currentPlayer, setCurrentPlayer] = useState(null);
  const [teams, setTeams] = useState([]);
  const [score, setScore] = useState(0);
  const [timeLeft, setTimeLeft] = useState(GAME_CONFIG.GAME_DURATION);
  const [feedback, setFeedback] = useState('');
  const [loading, setLoading] = useState(true);

  const timerRef = useRef(null);
  const feedbackTimeoutRef = useRef(null);

  // Load teams on mount
  useEffect(() => {
    loadTeams();
  }, []);

  // Start game timer
  useEffect(() => {
    if (teams.length > 0 && !currentPlayer) {
      loadRandomPlayer();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [teams]);

  // Timer countdown
  useEffect(() => {
    if (timeLeft > 0) {
      timerRef.current = setTimeout(() => {
        setTimeLeft(timeLeft - 1);
      }, 1000);
    } else {
      onGameEnd(score);
    }
    return () => clearTimeout(timerRef.current);
  }, [timeLeft, score, onGameEnd]);

  const loadTeams = async () => {
    try {
      const data = await apiService.getTeams();
      setTeams(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error loading teams:', error);
      setTeams([]);
    }
  };

  const loadRandomPlayer = async () => {
    try {
      setLoading(true);
      const player = await apiService.getRandomPlayer();
      setCurrentPlayer(player);
      setLoading(false);
    } catch (error) {
      console.error('Error loading player:', error);
      setLoading(false);
    }
  };

  const handleTeamSelect = (teamName) => {
    if (feedback) return; // Prevent multiple clicks

    const isCorrect = teamName === currentPlayer.team_name;
    const points = isCorrect ? GAME_CONFIG.CORRECT_POINTS : GAME_CONFIG.INCORRECT_POINTS;

    setScore(prevScore => prevScore + points);
    setFeedback(
      isCorrect
        ? `✅ Correct! +${GAME_CONFIG.CORRECT_POINTS} points`
        : `❌ Wrong! ${currentPlayer.firstname} ${currentPlayer.lastname} plays for ${currentPlayer.team_name}. ${GAME_CONFIG.INCORRECT_POINTS} points`
    );

    // Load next player after delay
    feedbackTimeoutRef.current = setTimeout(() => {
      setFeedback('');
      loadRandomPlayer();
    }, 2000);
  };

  // Cleanup
  useEffect(() => {
    return () => {
      clearTimeout(timerRef.current);
      clearTimeout(feedbackTimeoutRef.current);
    };
  }, []);

  if (loading || !currentPlayer) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-white text-2xl bg-black bg-opacity-50 px-8 py-4 rounded-lg">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen p-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-lg p-4 md:p-6 mb-6 flex justify-between items-center">
          <div
            className={`flex items-center transition-colors duration-300 ${
              timeLeft <= 10 ? 'animate-pulse' : ''
            }`}
            role="timer"
            aria-live="polite"
            aria-atomic="true"
          >
            <Clock className={`w-6 h-6 md:w-8 md:h-8 mr-2 md:mr-3 ${
              timeLeft <= 10 ? 'text-red-600' : timeLeft <= 30 ? 'text-orange-500' : 'text-blue-500'
            }`} aria-hidden="true" />
            <span
              className={`text-2xl md:text-3xl font-bold ${
                timeLeft <= 10 ? 'text-red-600' : timeLeft <= 30 ? 'text-orange-500' : 'text-gray-700'
              }`}
              aria-label={`${timeLeft} seconds remaining`}
            >
              {timeLeft}s
            </span>
          </div>
          <div className="text-right" role="status" aria-live="polite">
            <div className="text-xs md:text-sm text-gray-500 uppercase tracking-wide mb-1">
              Score
            </div>
            <div className="text-2xl md:text-3xl font-bold text-blue-600" aria-label={`Current score: ${score} points`}>
              {score}
            </div>
          </div>
        </div>

        {/* Player Card */}
        <PlayerCard
          player={currentPlayer}
          feedback={feedback}
        />

        {/* Team Selector */}
        <TeamSelector
          teams={teams}
          onTeamSelect={handleTeamSelect}
          disabled={!!feedback}
        />
      </div>
    </div>
  );
};

export default GameScreen;