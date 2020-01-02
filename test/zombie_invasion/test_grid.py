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
    grid.add_human(mock_human, starting_coordinates)
    assert [1, 2] == grid.human_coordinates[mock_human]


def test_add_human_off_grid():
    """
    A player should not be able to be added out of bounds
    """
    mock_human = Mock()
    starting_coordinates = [5, 5]
    grid = Grid(size=[4, 4])
    with pytest.raises(ValueError):
        grid.add_human(mock_human, starting_coordinates)


def test_display_empty_grid():
    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([row, row, row, row])

    grid = Mock(width=4, length=4, human_coordinates={}, zombie_coordinates={})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_human_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "H", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_human = Mock(render="H")
    grid = Mock(width=4, length=4, human_coordinates={mock_human: [1, 1]}, zombie_coordinates={})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_zombie_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "Z", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_zombie = Mock(render="Z")
    grid = Mock(width=4, length=4, human_coordinates={}, zombie_coordinates={mock_zombie: [1, 1]})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)

