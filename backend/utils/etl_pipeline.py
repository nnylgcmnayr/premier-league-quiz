from .data_loader import *

def etl_data():
    """
    Create a Data Loader object to get data for application
    """
    data_loader = DataLoader() # Initialize data loader

    # Get relevant instance variables from the data loader
    player_info = data_loader.get_player_info()
    players_dict = data_loader.get_player_dict()
    teams_list = data_loader.get_team_list()
    trackable_stats = data_loader.get_trackable_stats()
    games_list = data_loader.get_games_list()

    return players_dict