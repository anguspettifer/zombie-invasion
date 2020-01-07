import random

from zombie_invasion.grid import Grid
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


class Game:

    def __init__(self):
        self.dimensions = None
        self.number_of_humans = None
        self.number_of_zombies = None
        self.grid = None

    def _request_dimensions(self):
        print("Please enter dimensions")
        self.dimensions = input()

    def _request_number_of_humans(self):
        print("Please enter number of humans")
        self.number_of_humans = input()

    def _request_number_of_zombies(self):
        print("Please enter number of zombies")
        self.number_of_zombies = input()

    def _add_players(self, player_class, number_of_players):
        for i in range(number_of_players):
            x_coordinate = random.randint(0, self.grid.width)
            y_coordinate = random.randint(0, self.grid.length)
            self.grid.add_player(player_class(), (x_coordinate, y_coordinate))

    def set_up(self):
        self._request_dimensions()
        self._request_number_of_humans()
        self._request_number_of_zombies()

        self.grid = Grid(self.dimensions)
        self._add_players(Human, self.number_of_humans)
        self._add_players(Zombie, self.number_of_zombies)

