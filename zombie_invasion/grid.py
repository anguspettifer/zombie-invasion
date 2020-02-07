from copy import copy

from zombie_invasion.conversion import Conversion
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


class Grid:
    """Knows which players are where in the grid"""

    def __init__(self, size):
        self.width = size[0] - 1
        self.length = size[1] - 1
        self.players_and_coordinates = {}
        self.unoccupied_coordinates = [[x, y] for x in range(size[0]) for y in range(size[1])]  # Lack of single source of truth??

    def add_player(self, player, coordinates):
        """
        Adds a player to the dictionary of the player type, along with the starting coordinates
        """
        if coordinates[0] > self.width or coordinates[1] > self.length:
            raise ValueError
        self.players_and_coordinates[player] = coordinates
        try:
            self.unoccupied_coordinates.remove(coordinates)
        except ValueError:
            # It's ok to add two players on the same square
            # I'm not explicitly allowing humans as grid is not responsible for the rules of the game
            pass

    def players_move(self):
        for player, coordinates in self.players_and_coordinates.items():
            self.players_and_coordinates[player] = player.move(
                coordinates,
                grid_dimensions=[self.width, self.length],
                players_and_coordinates=copy(self.players_and_coordinates)
            )

    @staticmethod
    def _get_unique(iterable):
        result = []
        for item in iterable:
            if item not in result:
                result.append(item)
        return result

    def convert_if_needed(self):
        """
        If a human and zombie have the same coordinates
        The human is removed and a new zombie is instansiated with those coordinates
        """
        humans_and_coordinates = {k: v for k, v in self.players_and_coordinates.items() if type(k) == Human}
        zombies_and_coordinates = {k: v for k, v in self.players_and_coordinates.items() if type(k) == Zombie}

        conversion = Conversion(humans_and_coordinates, zombies_and_coordinates, Human, Zombie)
        conversion.convert()

        self.players_and_coordinates = {**conversion.source_items, **conversion.destination_items}
