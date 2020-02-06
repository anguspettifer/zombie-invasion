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

    def _add_humans(self, player_class, number_of_players):
        """
        Randomly choose any x and y coordinates in the grid
        Add a new human on that square
        """
        for i in range(number_of_players):
            x_coordinate = random.randint(0, self.grid.width)
            y_coordinate = random.randint(0, self.grid.length)
            self.grid.add_player(player_class(), [x_coordinate, y_coordinate])

    def _add_zombies(self, number_of_players):
        """
        Randomly choose any unoccupied coordinates from the grid
        Add a new zombie to that square
        """
        for i in range(number_of_players):
            coordinates = random.choice(self.grid.unoccupied_coordinates)
            self.grid.add_player(Zombie(), coordinates)

    def set_up(self):
        """
        Request set up information from user
        Instantiate grid with information
        Add players at specific coordinates
        """
        self._request_dimensions()
        self._request_number_of_humans()
        self._request_number_of_zombies()

        self.grid = Grid(self.dimensions)
        self._add_humans(Human, self.number_of_humans)
        self._add_humans(Zombie, self.number_of_zombies)

    def initial_display(self):
        Display(self.grid).initial_display()

    def play(self):
        """
        While there are humans
        Display the grid
        Move all the players
        """
        while len(self.grid.human_coordinates) > 0:
            self.number_of_humans = len(self.grid.human_coordinates)
            self.number_of_zombies = len(self.grid.zombie_coordinates)
            Display(self.grid).game_display(self.number_of_humans, self.number_of_zombies)
            self.grid.humans_move()
            self.grid.zombies_move()
            self.grid.convert_if_needed()
            self.number_of_turns += 1
            sleep(0.4)

        self.number_of_humans = len(self.grid.human_coordinates)
        self.number_of_zombies = len(self.grid.zombie_coordinates)
        Display(self.grid).end_game_display(self.number_of_humans, self.number_of_humans, self.number_of_turns)

