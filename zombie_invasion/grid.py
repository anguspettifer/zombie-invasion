from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


class Grid:
    """Knows which players are where in the grid"""

    def __init__(self, size):
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
        if coordinates[0] > (self.width - 1) or coordinates[1] > (self.length - 1):
            raise ValueError
        self.player_map[player.render][player] = coordinates

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

        # humans_to_delete = []
        # zombie_coords_to_add = []
        # current_humans = list(self.human_coordinates.keys())
        # attacking_zombies = list(self.zombie_coordinates.keys())
        # for human in current_humans:
        #     # The reason this doesn't work is because when we iterate though zombies, on the second run through it doesn't iterate as we have already removed the firs item
        #     # If it DID iterate it would still be an issue as we would be looking
        #     for zombie in attacking_zombies:
        #         if self.human_coordinates[human] == self.zombie_coordinates[zombie]:
        #             humans_to_delete.append(current_humans.pop(current_humans.index(human)))
        #             zombie_coords_to_add.append(attacking_zombies.pop(attacking_zombies.index(zombie)))
        #
        # for human in humans_to_delete:
        #     try:
        #         self.human_coordinates.pop(human)
        #     except KeyError:
        #         # 2 zombies are attacking the same human
        #         continue
        #
        # for zombie in zombie_coords_to_add:
        #     self.zombie_coordinates[Zombie()] = self.zombie_coordinates[zombie]
        #
        # # for human, human_coords in self.human_coordinates.items():
        # #     for zombie, zombie_coords in self.zombie_coordinates.items():
        # #         if human_coords == zombie_coords and zombie_coords not in zombie_coords_to_add:
        # #             humans_to_delete.append(human)
        # #             zombie_coords_to_add.append(human_coords)
        #
        # #
        # # for coords in self._get_unique(zombie_coords_to_add):
        # #     self.zombie_coordinates[Zombie()] = coords


class Conversion:
    """ Knows how to convert source object to destination based on matching criteria """
    def __init__(self, source_items, destination_items, source_object, destination_object):
        self.source_items = source_items
        self.destination_items = destination_items
        self.source_object = source_object
        self.destination_object = destination_object
        self.source_items_and_counters = {}
        self._sharing_squares()

    def _sharing_squares(self):
        """Given a source item, returns the number of destination items and other source items with the same criteria"""

        for source in self.source_items:
            source_criteria = self.source_items[source]
            number_source_objects = len([k for k in self.source_items if self.source_items[k] == source_criteria])
            number_destination_object = len([k for k in self.destination_items if self.destination_items[k] == source_criteria])
            self.source_items_and_counters[source] = (source_criteria, [number_source_objects, number_destination_object])

    def convert(self):
        criteria_and_sources_to_delete = dict()
        for source_instance, value in self.source_items_and_counters.items():
            if tuple(value[0]) in criteria_and_sources_to_delete:
                continue
            number_of_sources_to_convert = min([value[1][0], value[1][1]])
            for i in range(number_of_sources_to_convert):
                self.destination_items[self.destination_object()] = value[0]
                # I have to turn the dict key into a tuple as you can't search a dict if its keys are lists because lists are not hashable
                criteria_and_sources_to_delete[tuple(value[0])] = number_of_sources_to_convert

        sources_to_delete = []
        for criteria, number in criteria_and_sources_to_delete.items():
                for key, value in self.source_items.items():
                    if criteria == value:
                        sources_to_delete.append(key)
                        number -= 1
                        if number == 0: break

        for source in sources_to_delete: del self.source_items[source]

        # TODO: Can we use reduce??
