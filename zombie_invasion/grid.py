import pandas as pd
import random


class Grid:
    """Knows how to store players in a grid"""
    POSSIBLE_MOVES = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def __init__(self, size):
        self.width = size[0]
        self.length = size[1]
        self.coordinates = {} # maybe this could have some sort of ordering

    def add_player(self, player, coordinates):
        if coordinates[0] > self.width or coordinates[1] > self.length:
            raise ValueError
        self.coordinates[player] = coordinates

    def _get_new_coordinates(self, coordinates):
        move = self.POSSIBLE_MOVES[random.randint(0, 7)]
        if move == [0, -1]:
            print('')
        for i in range(0, 2):
            coordinates[i] += move[i]
            if coordinates[i] < 0:
                coordinates[i] = 0
        if coordinates[0] > self.width:
            coordinates[0] = self.width
        if coordinates[1] > self.length:
            coordinates[1] = self.length
        return coordinates

    def human_move(self):
        for player, coordinates in self.coordinates.iteritems():
            if player.render == "H":
                new_coordinates = self._get_new_coordinates(coordinates)
                self.coordinates[player] = new_coordinates

    @staticmethod
    def _move_one_closer(x, y):
        if x > y:
            return x - 1
        elif x < y:
            return x + 1
        else:
            return x

    def zombie_move(self):
        for player, coordinates in self.coordinates.iteritems():
            if player.render == "H":
                closest_human_coordinates = self.coordinates[player]
        for player, coordinates in self.coordinates.iteritems():
            if player.render == "Z":
                new_x_coordinate = self._move_one_closer(coordinates[0], closest_human_coordinates[0])
                new_y_coordinate = self._move_one_closer(coordinates[1], closest_human_coordinates[1])
                self.coordinates[player] = [new_x_coordinate, new_y_coordinate]


class Display:
    """Knows how to display a grid"""
    def __init__(self, grid):
        self.grid = grid

    def _create_empty_df(self):
        empty_row = ["." for i in range(self.grid.width)]
        return pd.DataFrame(data=[empty_row for i in range(self.grid.length)])

    def _add_objects(self, df):
        for object, coordinates in self.grid.coordinates.iteritems():
            df[coordinates[0]].loc[coordinates[1]] = object.render
        return df

    def render(self):
        df = self._create_empty_df()
        return self._add_objects(df)
