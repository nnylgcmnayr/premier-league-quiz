import datetime


class Players:

    def __init__(self, player_id, firstname, lastname, team_id, birthdate, position_id):
        self.player_id = player_id
        self.firstname = firstname
        self.lastname = lastname
        self.team_id = team_id
        self.team_name = None # Set via the DataLoader class
        self.birthdate = birthdate
        self.position_id = position_id
        self.position = None # Set via the DataLoader class
        self.age = self.set_age()

    # Getters for all instance variables
    def get_player_id(self):
        return self.player_id

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_team_id(self):
        return self.team_id

    def get_birthdate(self):
        return self.birthdate

    def get_position_id(self):
        return self.position_id

    def get_age(self):
        return self.age

    def get_team_name(self):
        return self.team_name

    # Setters needed
    def set_age(self):
        """
        Return the age in years with no remainder or decimal.
        :return: age in years as an int with no remainder or whole number
        """
        try:
            today = datetime.date.today()  # Get today's date as a datetime object
            date_2 = datetime.date(int(self.birthdate[:4]), int(self.birthdate[5:7]),
                                   int(self.birthdate[8:]))  # Get players date formatted as a datetime object
            age = (today - date_2) / 365  # Get player age as datetime timedelta object

            # Cast datetime timedelta object to int object to drop any remainder so it is only a whole number
            return int(age.days)
        except TypeError:
            return 'Unknown'

    # Magic method
    def __str__(self):

        return (self.firstname + ' ' + self.lastname +
                '\n' + 'Team Name: ' + self.team_name +
                '\n' + 'Age: ' + str(self.age) +
                '\n' + 'Position: ' + str(self.position))





