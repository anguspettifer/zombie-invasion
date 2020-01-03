import random
import math


class Zombie:
    def __init__(self):
        """
        Once a zombie starts hunting a human, it keeps hunting it and so needs to know that attribute.
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
    def _human_coordinates_and_absolute_distances(human_coordinates, zombie_coordinates):
        human_coordinates_distance = []
        for human, coordinates in human_coordinates.items():
            distance = abs(zombie_coordinates[0] - coordinates[0]) + abs(zombie_coordinates[1] - coordinates[1])
            human_coordinates_distance.append((human, coordinates, distance))

        return human_coordinates_distance

    @staticmethod
    def _closest_human_coordinates(zombie_coordinates, human_coordinates):
        """
        Checks the distance of all the humans from the zombie
        Returns the coordinates of all the equidistant closest humans
        """
        closest_humans_and_coordinates = {}
        human_coordinates_distance = []
        min_distance = math.inf

        for human, coordinates in human_coordinates.items():
            distance = abs(zombie_coordinates[0] - coordinates[0]) + abs(zombie_coordinates[1] - coordinates[1])
            min_distance = distance if distance <= min_distance else min_distance
            human_coordinates_distance.append((human, coordinates, distance))

        for human, coordinates, distance in human_coordinates_distance:
            # TODO: must be a way to edit the old dict rather than create a new one
            if distance == min_distance:
                closest_humans_and_coordinates[human] = coordinates

        return closest_humans_and_coordinates

    def move(self, zombie_coordinates, human_coordinates):
        """
        A zombie moves 1 square closer to the nearest human
        If more than one human is closest it moves to one them at random
        """
        closest_humans_and_coordinates = self._closest_human_coordinates(zombie_coordinates, human_coordinates)
        if self.__hunted_human not in closest_humans_and_coordinates.keys():
            self.__hunted_human = random.choice(list(closest_humans_and_coordinates))

        closest_human_coordinates = closest_humans_and_coordinates[self.__hunted_human]

        new_x_coordinates = self._move_one_closer(zombie_coordinates[0], closest_human_coordinates[0])
        new_y_coordinates = self._move_one_closer(zombie_coordinates[1], closest_human_coordinates[1])

        return [new_x_coordinates, new_y_coordinates]
