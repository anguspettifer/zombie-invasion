import pandas as pd


class Display:
    """Knows how to display a grid"""
    def __init__(self, grid):
        self.grid = grid

    def create_empty_df(self):
        empty_row = ["." for i in range(self.grid.width + 1)]
        return pd.DataFrame(data=[empty_row for i in range(self.grid.length + 1)])

    def _add_objects(self, df):
        # This method isn't dry. And it knows a lot about grid.
        for player, human_coordinates in self.grid.human_coordinates.items():
            df[human_coordinates[0]].loc[human_coordinates[1]] = player.render

        for player, zombie_coordinates in self.grid.zombie_coordinates.items():
            df[zombie_coordinates[0]].loc[zombie_coordinates[1]] = player.render
        return df

    def render(self):
        df = self.create_empty_df()
        return self._add_objects(df)
