import pandas as pd
from mock import Mock
from pandas.util.testing import assert_frame_equal

from zombie_invasion.display import Display


def test_display_empty_grid():
    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([row, row, row, row])

    grid = Mock(width=3, length=3, human_coordinates={}, zombie_coordinates={})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_human_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "H", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_human = Mock(render="H")
    grid = Mock(width=3, length=3, human_coordinates={mock_human: [1, 1]}, zombie_coordinates={})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_zombie_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "Z", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_zombie = Mock(render="Z")
    grid = Mock(width=3, length=3, human_coordinates={}, zombie_coordinates={mock_zombie: [1, 1]})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_no_humans():
    row = [".", ".", ".", "."]
    second_row = [".", "Z", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_zombie = Mock(render="Z")
    grid = Mock(width=3, length=3, human_coordinates={}, zombie_coordinates={mock_zombie: [1, 1]})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)