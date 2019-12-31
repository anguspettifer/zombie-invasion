import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal

from zombie_invasion.grid import Grid, Display
from mock import Mock, patch


def test_initializes_with_grid_size():
    grid = Grid(size=[4, 4])
    assert grid.length == 4
    assert grid.width == 4


def test_add_human():
    mock_human = Mock()
    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_human, starting_coordinates)
    assert [1, 2] == grid.coordinates[mock_human]


def test_add_human_off_grid():
    """
    A player should not be able to be added out of bounds
    """
    mock_human = Mock()
    starting_coordinates = [5, 5]
    grid = Grid(size=[4, 4])
    with pytest.raises(ValueError):
        grid.add_player(mock_human, starting_coordinates)


def test_grid_everybody_move_player_moves_randomly():
    mock_player = Mock()
    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_player, starting_coordinates)

    grid.everybody_move()
    possible_x_coords = [0, 1, 2]
    possible_y_coords = [1, 2, 3]
    assert grid.coordinates[mock_player][0] in possible_x_coords
    assert grid.coordinates[mock_player][1] in possible_y_coords
    assert grid.coordinates[mock_player] != [1, 2]


@patch("zombie_invasion.grid.random")
def test__get_new_coordinates_are_not_the_same(mock_random):
    """
    A human should move and should not stay still
    """
    mock_random.randint.return_value = 0

    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    new_coordinates = grid._get_new_coordinates(starting_coordinates)
    assert new_coordinates != [1, 2]


@patch("zombie_invasion.grid.random")
def test_human_cannot_move_through_grid_wall(mock_random):
    """
    If a human tries to move through a wall it must remain where it was in that dimension
    """
    mock_random.randint.return_value = 0

    mock_player = Mock()
    starting_coordinates = [0, 0]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_player, starting_coordinates)

    grid.everybody_move()
    assert grid.coordinates[mock_player] == starting_coordinates


def test_display_empty_grid():
    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([row, row, row, row])

    grid = Mock(width=4, length=4, coordinates={})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_human_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "H", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_human = Mock(render="H")
    grid = Mock(width=4, length=4, coordinates={mock_human: [1, 1]})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_zombie_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "Z", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_zombie = Mock(render="Z")
    grid = Mock(width=4, length=4, coordinates={mock_zombie: [1, 1]})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)
