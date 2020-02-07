import random
import math

from zombie_invasion.human import Human


class Zombie:
    def __init__(self):
        """
        Once a zombie starts hunting a human, it keeps hunting it.
        Thus it needs to remember the human it is hunting.
        Initially it is not hunting a human.
        """
        self.__hunted_human = None
        self.render = 'Z'

    @staticmethod
    def _move_one_closer(x, y):
        if x > y:
            return x - 1
        elif x < y:
            return x + 1
        else:
            return x

    @staticmethod
    def _closest_human_coordinates(zombie_coordinates, human_coordinates):
        """
        Checks the distance of all the humans from the zombie
        Returns the human objects and coordinates of all the equidistant closest humans
        """
        closest_humans_and_coordinates = {}
        human_coordinates_distance = []
        min_distance = math.inf

        for human, coordinates in human_coordinates.items():
            distance = abs(zombie_coordinates[0] - coordinates[0]) + abs(zombie_coordinates[1] - coordinates[1])
            min_distance = distance if distance <= min_distance else min_distance
            human_coordinates_distance.append((human, coordinates, distance))

        for human, coordinates, distance in human_coordinates_distance:
            if distance == min_distance:
                closest_humans_and_coordinates[human] = coordinates

        return closest_humans_and_coordinates

    def move(self, zombie_coordinates, grid_dimensions=None, players_and_coordinates=None):
        """
        A zombie moves 1 square closer to the nearest human
        If more than one human is closest it moves to one them at random
        The hunted human will be stored in memory

        Args:
            zombie_coordinates: a list of x-coordinate and y-coordinate of the zombie
            human_coordinates: a list of dictionaries of all human objects and their x and y coordinates

        Returns:
            A list of new x and y coordinates
        """
        human_coordinates = {k: v for k, v in players_and_coordinates.items() if type(k) == Human}
        closest_humans_and_coordinates = self._closest_human_coordinates(zombie_coordinates, human_coordinates)
        if self.__hunted_human not in closest_humans_and_coordinates.keys():
            self.__hunted_human = random.choice(list(closest_humans_and_coordinates))

        closest_human_coordinates = closest_humans_and_coordinates[self.__hunted_human]

        new_x_coordinates = self._move_one_closer(zombie_coordinates[0], closest_human_coordinates[0])
        new_y_coordinates = self._move_one_closer(zombie_coordinates[1], closest_human_coordinates[1])

        return [new_x_coordinates, new_y_coordinates]
