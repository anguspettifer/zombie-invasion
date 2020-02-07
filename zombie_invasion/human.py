import random


class Human:
    """Knows how a human renders and moves"""
    POSSIBLE_MOVES = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def __init__(self):
        self.render = 'H'

    def move(self, coordinates, grid_dimensions, players_and_coordinates=None):
        """
        A human moves 1 space randomly to any adjacent space unless there is a wall
        """
        move = self.POSSIBLE_MOVES[random.randint(0, 7)]
        for i in range(0, 2):  # 0 = x axis, 1 = y axis
            coordinates[i] += move[i]
            if coordinates[i] < 0:
                coordinates[i] = 0
            if coordinates[i] > grid_dimensions[i]:
                coordinates[i] = grid_dimensions[i]
        return coordinates
