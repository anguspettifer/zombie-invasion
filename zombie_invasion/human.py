import random
from copy import copy


class Human:
    """Knows how a human renders and moves"""
    POSSIBLE_DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def __init__(self, speed=1):
        self.render = 'H'
        self.speed = speed

    @staticmethod
    def _move_one_square(coordinates, grid_dimensions, direction):
        """
        A human moves 1 space randomly to any adjacent space unless there is a wall
        """
        for i in range(0, 2):  # 0 = x axis, 1 = y axis
            coordinates[i] += direction[i]
            if coordinates[i] < 0:
                coordinates[i] = 0
            if coordinates[i] > grid_dimensions[i]:
                coordinates[i] = grid_dimensions[i]
        return coordinates

    def move(self, coordinates, grid_dimensions, players_and_coordinates=None):
        """
        A human moves x space randomly where x = speed
        """

        direction = self.POSSIBLE_DIRECTIONS[random.randint(0, 7)]

        for i in range(self.speed):
            coordinates = self._move_one_square(coordinates, grid_dimensions, direction)

        return coordinates
