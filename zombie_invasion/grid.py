import pandas as pd


class Grid:
    """Knows how to store players in a grid"""
    def __init__(self, size):
        self.width = size[0]
        self.length = size[1]
        self.coordinates = {}

    def add_player(self, human, coordinates):
        self.coordinates[human] = coordinates

    def everybody_move(self):
        for human, coordinates in self.coordinates.iteritems():
            new_coordinates = [coordinates[0] - 1, coordinates[1]]
            self.coordinates[human] = new_coordinates


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
