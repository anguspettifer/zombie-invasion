import pandas as pd
from mock import patch
from pandas.util.testing import assert_frame_equal

from zombie_invasion.grid import Grid, Display
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie

"""
As a viewer
I can watch a human and zombie on the playing grid
So that I can be amused
"""


def test_grid_renders():
    # Given the means to start the program
    # When the user initiates the start
    # Then a 4x3 grid is rendered on the screen
    grid = Grid(size=[4, 3])
    display = Display(grid)

    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([row, row, row])

    assert_frame_equal(display.render(), expected_df)


def test_grid_renders_with_human():
    # Given the means to start the program
    # When the user initiates the start
    # Then a human is occupying a single square

    human = Human()
    grid = Grid(size=[4, 3])
    grid.add_player(human, [0, 0])
    display = Display(grid)

    top_row = ["H", ".", ".", "."]
    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([top_row, row, row])

    assert_frame_equal(display.render(), expected_df)


def test_grid_renders_with_zombie():
    # Given the means to start the program
    # When the user initiates the start
    # Then a zombie is occupying a single square

    zombie = Zombie()
    grid = Grid(size=[4, 3])
    grid.add_player(zombie, [0, 0])
    display = Display(grid)

    top_row = ["Z", ".", ".", "."]
    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([top_row, row, row])

    assert_frame_equal(display.render(), expected_df)


def test_grid_renders_with_zombie_and_human():
    # Given the means to start the program
    # When the user initiates the start
    # Then the human and zombie are on different squares

    zombie = Zombie()
    human = Human()
    grid = Grid(size=[4, 3])
    grid.add_player(zombie, [0, 0])
    grid.add_player(human, [0, 2])
    display = Display(grid)
    rendered_display = display.render()

    top_row = ["Z", ".", ".", "."]
    bottom_row = ["H", ".", ".", "."]
    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([top_row, row, bottom_row])

    assert_frame_equal(rendered_display, expected_df)


"""
As a viewer
I can watch a human move in a random
So that I can be amused**
"""


def test_human_moves_one_space():
    #TODO: to ask andy. There were times when this test passed and failed randomly
    # Given a program in progress
    # When it is time for a new go or turn
    # Then the human will move 1 pace in a random direction (N, NE, E, SE, S, SW, W, NW)
    human = Human()
    grid = Grid(size=[4, 3])
    grid.add_player(human, [2, 1])
    grid.everybody_move()
    display = Display(grid)
    rendered_display = display.render()

    possible_human_coordinates = [[2, 0], [3, 0], [3, 1], [3, 2], [2, 2], [1, 2], [1, 1], [1, 0]]
    result = []
    for coordinates in possible_human_coordinates:
        result.append(rendered_display[coordinates[0]].loc[coordinates[1]])
    assert "H" in result


@patch("zombie_invasion.grid.random")
def test_human_does_not_move_if_wall(mock_random):
    # Given a program in progress
    # When a human moves into a wall
    # Then the human will not move on that go
    mock_random.randint.return_value = 0
    human = Human()
    grid = Grid(size=[4, 3])
    grid.add_player(human, [0, 0])
    grid.everybody_move()
    display = Display(grid)
    rendered_display = display.render()
    assert rendered_display[0].loc[0] == "H"

