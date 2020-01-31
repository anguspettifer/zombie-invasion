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

    def initial_display(self):
        print(f"Please adjust screen to the size of the below grid:\n{self.create_empty_df()}\nplease hit enter")
        input()

    def game_display(self, number_of_humans, number_of_zombies):
        print(f"Human count: {number_of_humans} \nZombie count: {number_of_zombies} \n {self.render()}")

    def end_game_display(self, number_of_humans, number_of_zombies, number_of_turns):
        print(f"Human count: {number_of_humans}\nZombie count: {number_of_zombies}\n{self.render()}\n"
              f"Number of turns: {number_of_turns}\nHumans extinct!")
