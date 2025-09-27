
class Games:

    def __init__(self, kickoff_date, away_team_id, home_team_id, away_team_goals, home_team_goals, completed):
        self.kickoff_date = kickoff_date
        self.away_team_id = away_team_id
        self.away_team_name = None
        self.home_team_id = home_team_id
        self.home_team_name = None
        self.away_team_goals = away_team_goals
        self.home_team_goals = home_team_goals
        self.completed = completed


    def get_away_team_id(self):
        return self.away_team_id

    def get_home_team_id(self):
        return self.home_team_id

    def get_kickoff_date(self):
        return self.kickoff_date

    def get_completed(self):
        return self.completed


    def __str__(self):

        if self.get_completed():
            a_game = (self.home_team_name + ' (Home)' + ' vs. ' + self.away_team_name + ' (Away)' + ' Date/Time: ' + self.kickoff_date +
                  '\n' + 'Result: ' + str(self.home_team_goals) + ' - ' + str(self.away_team_goals)) # + '------ ' + str(self.get_completed())
            return a_game

        else:
            a_game = (self.home_team_name + ' (Home)' + ' vs. ' + self.away_team_name + ' (Away)' + ' Date/Time: ' + self.kickoff_date) # + '------ ' + str(self.get_completed())
            return a_game
