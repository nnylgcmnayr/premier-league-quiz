import requests, json
from .players import *
from .teams import *
from .games import *

class DataLoader:

    def __init__(self):
        """Load data and break it out between instance variables"""
        self.bootstrap_request = self.process_bootstrap_static()
        self.fixtures_request = self.process_fixtures_static()
        self.team_info = self.set_team_info()
        self.player_info = self.set_player_info()


        self.team_list = self.load_all_teams_to_list()
        self.position_key = self.position_setter()
        self.trackable_stats = self.stat_setter()
        self.games_list = self.load_all_games_to_list()


        # Used by API
        self.player_dict = self.load_all_players_to_dict()
        self.teams_dict = self.load_all_teams_to_dict()


    # Make API calls for data
    @staticmethod
    def process_bootstrap_static():
        """
        Make a request to the API for general information.
        :return: The player info and teams list
        """
        # base url for all FPL API endpoints
        base_url = 'https://fantasy.premierleague.com/api/'

        # get data from bootstrap-static endpoint
        r = requests.get(base_url + 'bootstrap-static/').json()

        return r

    @staticmethod
    def process_fixtures_static():
        """
        Make a request to the API for fixture data.
        :return: List of all 380 matches in current season
        """
        # base url for all FPL API endpoints
        base_url = 'https://fantasy.premierleague.com/api/'

        # get data from bootstrap-static endpoint
        r = requests.get(base_url + 'fixtures').json()

        return r # List of all 380 matches in current season

    # Setters for all instance variables
    def set_team_info(self):
        # The value of the Teams key is a list of dictionaries. Each team has a dictionary
        team_info = self.bootstrap_request['teams']

        return team_info

    def load_all_teams_to_list(self):

        team_list = [Teams(i['name'], i['id'], i['position']) for i in self.team_info]
        return team_list

    def position_setter(self):

        position_data = self.bootstrap_request['element_types']

        id_position_key = {}

        for i in position_data:
            x = i['id']
            y = i['singular_name']
            id_position_key[x] = y

        return id_position_key

    def stat_setter(self):

        elements_stats = self.bootstrap_request['element_stats']

        stat_keys = {}
        for i in elements_stats:
            x = i['name']
            y = i['label']
            stat_keys[x] = y

        return stat_keys

    def load_all_games_to_list(self):

        # Load all games into a list
        games_list = [Games(item['kickoff_time'], item['team_a'], item['team_h'],
                            item['team_a_score'], item['team_h_score'], item['finished']) for item in self.fixtures_request]

        # Loop through teams to set away and home team name
        for x in games_list:
            for i in self.get_team_list():
                if i.get_team_id() == x.get_away_team_id():
                    x.away_team_name = i.get_team_name()
                if i.get_team_id() == x.get_home_team_id():
                    x.home_team_name = i.get_team_name()

                # Add Team Points for completed games so far this season
                i.add_points_wins_loses_draws(x)

        return games_list

    def set_player_info(self):

        # The value of the Elements key is a list of dictionaries. Each player has a dictionary
        player_info = self.bootstrap_request['elements']  # Access the value of the Elements key from the r dictionary.

        return player_info

    def load_all_players_to_dict(self):

        # Load players into list with required data points
        players_list = [Players(i['id'], i['first_name'], i['second_name'], i['team'], i['birth_date'], i['element_type']) for i in self.player_info]

        # Loop through players to set additional player object variables
        for player in players_list:
            for team in self.get_team_list(): # Set player team name using team objects
                if player.get_team_id() == team.get_team_id():
                    player.team_name = team.get_team_name()
                    for x, y in self.position_key.items(): # Set player position using the positions key instance variable
                        if x == player.get_position_id():
                            player.position = y

        players_list = [{'player_id': i.player_id, 'firstname': i.firstname, 'lastname': i.lastname, 'team_id': i.team_id,
                         'team_name': i.team_name, 'birthdate': i.birthdate, 'position_id': i.position_id, 'position': i.position, 'age':i.age} for i in players_list]

        return players_list

    def load_all_teams_to_dict(self):
        teams_dict = [{'team_id': i.team_id, 'team_name': i.team_name, 'table_position': i.table_position, 'total_points': i.total_points,
                       'wins': i.wins, 'loses': i.loses, 'draws': i.draws} for i in self.team_list]
        return teams_dict

    # Getters for instance variables
    def get_player_info(self):
        return self.player_info

    def get_team_info(self):
        return self.team_info

    def get_team_list(self):
        return self.team_list

    def get_player_dict(self):
        return self.player_dict

    def get_trackable_stats(self):
        return self.trackable_stats

    def get_games_list(self):
        return self.games_list

    def get_teams_dict(self):
        return self.teams_dict


