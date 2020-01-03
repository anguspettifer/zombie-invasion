from zombie_invasion.zombie import Zombie


class Grid:
    """Knows which players are where in the grid"""

    def __init__(self, size):
        # TODO: coords should be tuples not lists
        self.width = size[0]
        self.length = size[1]
        self.human_coordinates = {}
        self.zombie_coordinates = {}
        self.player_map = {
            'H': self.human_coordinates,
            'Z': self.zombie_coordinates
        }

    def add_player(self, player, coordinates):
        """
        Adds a player to the dictionary of the player type, along with the starting coordinates
        """
        if coordinates[0] > self.width or coordinates[1] > self.length:
            raise ValueError
        self.player_map[player.render][player] = coordinates

    def human_move(self):
        #TODO: These 2 method could maybe be combined? and game is responsible for knowing the arguments
        for human, coordinates in self.human_coordinates.items():
            self.human_coordinates[human] = human.move(coordinates, [self.width, self.length])

    def zombie_move(self):
        for zombie, coordinates in self.zombie_coordinates.items():
            self.zombie_coordinates[zombie] = zombie.move(coordinates, self.human_coordinates)

    def convert_if_needed(self):
        # TODO: move to game class
        # TODO: 2 way dict class?
        for human, human_coords in self.human_coordinates.items():
            for zombie, zombie_coords in self.zombie_coordinates.items():
                if human_coords == zombie_coords:
                    human_to_delete = human
                    zombie_coords_to_add = human_coords
        self.human_coordinates.pop(human_to_delete)
        self.zombie_coordinates[Zombie()] = zombie_coords_to_add

