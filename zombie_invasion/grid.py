from zombie_invasion.conversion import Conversion
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


class Grid:
    """Knows which players are where in the grid"""

    def __init__(self, size):
        self.width = size[0] - 1
        self.length = size[1] - 1
        self.human_coordinates = {}
        self.zombie_coordinates = {}
        self.unoccupied_coordinates = [[x, y] for x in range(size[0]) for y in range(size[1])]  # Lack of single source of truth??
        self.player_map = {
            'H': self.human_coordinates,
            'Z': self.zombie_coordinates
        }

    def add_player(self, player, coordinates):
        """
        Adds a player to the dictionary of the player type, along with the starting coordinates
        """
        if coordinates[0] > (self.width) or coordinates[1] > (self.length):
            raise ValueError
        self.player_map[player.render][player] = coordinates
        try:
            self.unoccupied_coordinates.remove(coordinates)
        except ValueError:
            # It's ok to add two players on the same square
            # I'm not explicitly allowing humans as grid is not responsible for the rules of the game
            pass

    def humans_move(self):
        #TODO: These 2 method could maybe be combined? and game is responsible for knowing the arguments
        for human, coordinates in self.human_coordinates.items():
            self.human_coordinates[human] = human.move(coordinates, [self.width, self.length])

    def zombies_move(self):
        for zombie, coordinates in self.zombie_coordinates.items():
            self.zombie_coordinates[zombie] = zombie.move(coordinates, self.human_coordinates)

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
        conversion = Conversion(self.human_coordinates, self.zombie_coordinates, Human, Zombie)
        conversion.convert()
        self.human_coordinates = conversion.source_items
        self.zombie_coordinates = conversion.destination_items


