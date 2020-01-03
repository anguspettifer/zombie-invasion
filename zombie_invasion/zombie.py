import random
import math


class Zombie:
    def __init__(self):
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
    def _random_closest_human_coordinates(zombie_coordinates, human_coordinates):
        closest_humans = []
        human_coordinates_distance = []
        min_distance = math.inf
        for human, coordinates in human_coordinates.items():
            distance = abs(zombie_coordinates[0] - coordinates[0]) + abs(zombie_coordinates[1] - coordinates[1])
            min_distance = distance if distance <= min_distance else min_distance
            human_coordinates_distance.append((human, coordinates, distance))

        # min_distance = min([x[2] for x in human_coordinates_distance])

        for human, coordinates, distance in human_coordinates_distance:
            if distance == min_distance:
                closest_humans.append(coordinates)

        random_int = random.randint(0, len(closest_humans) - 1)

        return closest_humans[random_int]

    def move(self, zombie_coordinates, human_coordinates):
        """
        A zombie moves 1 square closer to the nearest human
        """
        random_closest_human_coordinates = self._random_closest_human_coordinates(zombie_coordinates, human_coordinates)

        new_x_coordinates = self._move_one_closer(zombie_coordinates[0], random_closest_human_coordinates[0])
        new_y_coordinates = self._move_one_closer(zombie_coordinates[1], random_closest_human_coordinates[1])
        return [new_x_coordinates, new_y_coordinates]
