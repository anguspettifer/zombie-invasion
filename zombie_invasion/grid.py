import pandas as pd


class Grid:
    """Knows how to store players in a grid"""
    POSSIBLE_MOVES = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def __init__(self, size):
        # TODO: coords should be tuples not lists
        self.width = size[0]
        self.length = size[1]
        self.human_coordinates = {}
        self.zombie_coordinates = {}

    def add_human(self, player, coordinates):
        if coordinates[0] > self.width or coordinates[1] > self.length:
            raise ValueError
        self.human_coordinates[player] = coordinates

    def add_zombie(self, player, coordinates):
        # TODO: Should I refactor this into one?
        if coordinates[0] > self.width or coordinates[1] > self.length:
            raise ValueError
        self.zombie_coordinates[player] = coordinates

    def human_move(self):
        for human, coordinates in self.human_coordinates.items():
            self.human_coordinates[human] = human.move(coordinates, [self.width, self.length])

    def zombie_move(self):
        for zombie, coordinates in self.zombie_coordinates.items():
            self.zombie_coordinates[zombie] = zombie.move(coordinates, self.human_coordinates)


class Display:
    """Knows how to display a grid"""
    def __init__(self, grid):
        self.grid = grid

    def _create_empty_df(self):
        empty_row = ["." for i in range(self.grid.width)]
        return pd.DataFrame(data=[empty_row for i in range(self.grid.length)])

    def _add_objects(self, df):
        for object, human_coordinates in self.grid.human_coordinates.items():
            df[human_coordinates[0]].loc[human_coordinates[1]] = object.render
        for object, zombie_coordinates in self.grid.zombie_coordinates.items():
            df[zombie_coordinates[0]].loc[zombie_coordinates[1]] = object.render
        return df

    def render(self):
        df = self._create_empty_df()
        return self._add_objects(df)
