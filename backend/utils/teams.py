
class Teams:

    def __init__(self, team_name, team_id, table_position):

        self.team_name = team_name
        self.team_id = team_id
        self.table_position = table_position
        self.total_points = 0
        self.wins = 0
        self.loses = 0
        self.draws = 0

    # Getters for instance variables
    def get_team_name(self):
        return self.team_name

    def get_team_id(self):
        return self.team_id

    def get_table_position(self):
        return self.table_position

    def add_points_wins_loses_draws(self, a_game):
        """
        Set the teams wins, loses, draws and total points.
        :param a_game: A game object
        :return: Nothing
        """
        if a_game.get_completed():
            if self.team_id == a_game.get_away_team_id():
                if a_game.away_team_goals > a_game.home_team_goals:
                    self.total_points += 3
                    self.wins += 1
                elif a_game.away_team_goals == a_game.home_team_goals:
                    self.total_points += 1
                    self.draws += 1
                else:
                    self.loses += 1
            elif self.team_id == a_game.get_home_team_id():
                if a_game.home_team_goals > a_game.away_team_goals:
                    self.total_points += 3
                    self.wins += 1
                elif a_game.home_team_goals == a_game.away_team_goals:
                    self.total_points += 1
                    self.draws += 1
                else:
                    self.loses += 1


    # Magic method
    def __str__(self):
        return (str(self.get_table_position()) + '. ' + self.get_team_name() + ', Points: ' + str(self.total_points) +
                '\n' + 'Wins: ' + str(self.wins) + ', Draws: ' + str(self.draws) + ', Loses: ' + str(self.loses))
