import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  // Get random player
  async getRandomPlayer() {
    const response = await api.get('/api/random-player');
    return response.data;
  },

  // Get all teams
  async getTeams() {
    const response = await api.get('/api/get-teams');
    return response.data;
  },

  // Submit score
  async submitScore(playerName, score, gameDuration = 60) {
    const response = await api.post('/api/scores', {
      player_name: playerName,
      score,
      game_duration: gameDuration,
    });
    return response.data;
  },

  // Get leaderboard
  async getLeaderboard(limit = 10) {
    const response = await api.get(`/api/leaderboard?limit=${limit}`);
    return response.data;
  },

  // // Get stats
  // async getStats() {
  //   const response = await api.get('/api/stats');
  //   return response.data;
  // },
};

export default apiService;