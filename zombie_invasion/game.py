import random
from time import sleep

from zombie_invasion.display import Display
from zombie_invasion.grid import Grid
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


class Game:
    """Knows the artifacts of the game, monitors human life, ends game on extinction"""

    def __init__(self):
        self.dimensions = None
        self.number_of_humans = None
        self.number_of_zombies = None
        self.grid = None
        self.number_of_turns = 0
        self.human_speed = 0

    def _request_dimensions(self):
        print("Please enter width")
        width = int(input())
        print("Please enter length")
        length = int(input())
        self.dimensions = (width, length)

    def _request_number_of_humans(self):
        print("Please enter number of humans")
        self.number_of_humans = int(input())

    def _request_number_of_zombies(self):
        print("Please enter number of zombies")
        self.number_of_zombies = int(input())

    def _request_human_speed(self):
        print("Please enter human speed. Number of squares covered per turn:")
        self.human_speed = int(input())

    def _add_humans(self, human_class=Human):  # Dependency injection to ease testing
        """
        Randomly choose any x and y coordinates in the grid
        Add a new human on that square
        Implement user_given human speed
        """
        for i in range(self.number_of_humans):
            x_coordinate = random.randint(0, self.grid.width)
            y_coordinate = random.randint(0, self.grid.length)
            self.grid.add_player(human_class(self.human_speed), [x_coordinate, y_coordinate])

    def _add_zombies(self, zombie_class=Zombie):  # Dependency injection to ease testing
        """
        Randomly choose any unoccupied coordinates from the grid
        Add a new zombie to that square
        """
        for i in range(self.number_of_zombies):
            try:
                coordinates = random.choice(self.grid.unoccupied_coordinates)
                self.grid.add_player(zombie_class(), coordinates)
            except IndexError: # No spaces left for zombies
                self.number_of_zombies = len([x for x in self.grid.players_and_coordinates.keys() if type(x) == Zombie])
                print(f"You have reached your zombie limit, {self.number_of_zombies} zombies added")

    def _update_number_of_players(self):
        self.number_of_zombies = len([x for x in self.grid.players_and_coordinates.keys() if type(x) == Zombie])
        self.number_of_humans = len([x for x in self.grid.players_and_coordinates.keys() if type(x) == Human])

    def set_up(self, grid_class=Grid):  # Dependency injection to ease testing
        """
        Request set up information from user
        Instantiate grid with information
        Add players at specific coordinates
        """
        self._request_dimensions()
        self._request_number_of_humans()
        self._request_number_of_zombies()
        self._request_human_speed()

        self.grid = grid_class(self.dimensions)
        self._add_humans()
        self._add_zombies()

    def initial_display(self):
        Display(self.grid).initial_display()

    def play(self, display_class=Display):
        """
        While there are humans
        Display the grid
        Move all the players
        """
        while self.number_of_humans > 0:
            Display(self.grid).game_display(self.number_of_humans, self.number_of_zombies)
            self.grid.players_move()
            self.grid.convert_if_needed()
            self._update_number_of_players()
            self.number_of_turns += 1
            sleep(0.4)

        display_class(self.grid).end_game_display(self.number_of_humans, self.number_of_zombies, self.number_of_turns)

