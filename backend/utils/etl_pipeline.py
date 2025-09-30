from .data_loader import *

def etl_data():
    """
    Create a Data Loader object to get data for application
    """
    data_loader = DataLoader() # Initialize data loader

    # Get relevant instance variables from the data loader
    players_dict = data_loader.get_player_dict()
    teams_dict = data_loader.get_teams_dict()

    trackable_stats = data_loader.get_trackable_stats()
    games_list = data_loader.get_games_list()

    return players_dict, teams_dict