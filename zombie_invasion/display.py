import pandas as pd


class Display:
    """Knows how to display a grid"""
    def __init__(self, grid):
        self.grid = grid

    def _create_empty_df(self):
        empty_row = ["." for i in range(self.grid.width + 1)]
        return pd.DataFrame(data=[empty_row for i in range(self.grid.length + 1)])

    def _add_objects(self, df):
        for object, human_coordinates in self.grid.human_coordinates.items():
            df[human_coordinates[0]].loc[human_coordinates[1]] = object.render

        for object, zombie_coordinates in self.grid.zombie_coordinates.items():
            df[zombie_coordinates[0]].loc[zombie_coordinates[1]] = object.render
        return df

    def render(self):
        df = self._create_empty_df()
        return self._add_objects(df)
