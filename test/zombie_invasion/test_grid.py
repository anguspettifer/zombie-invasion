import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal

from zombie_invasion.grid import Grid, BlankSquare, Row, Display
from mock import Mock


def test_square_renders_empty_by_default():
    starter_square = "|_|"
    square = BlankSquare(starter_square)
    assert square.render == "|_|"


def test_row_renders_4_squares():
    # I want to know that the grid renders a grid of squares
    # I don't want to care about the state of those squares
    # I just want to know that the square object is rendered
    square_1 = Mock(render="sq1")
    square_2 = Mock(render="sq2")
    square_3 = Mock(render="sq3")
    square_4 = Mock(render="sq4")

    squares = [square_1, square_2, square_3, square_4]

    row = Row(squares)
    playing_row = row.render
    assert playing_row == "sq1sq2sq3sq4"


def test_row_human_in_row():
    square_1 = Mock(render="sq1")
    square_3 = Mock(render="sq3")
    square_4 = Mock(render="sq4")
    human = Mock(render="H")
    squares = [square_1, human, square_3, square_4]
    row = Row(squares)

    assert row.human_in_row == [1]


def test_row_move_left():
    square_1 = Mock(render="sq1")
    square_3 = Mock(render="sq3")
    square_4 = Mock(render="sq4")
    human = Mock(render="H")
    squares = [square_1, human, square_3, square_4]
    row = Row(squares)

    row.move_left()

    assert row.human_in_row == [0]



@pytest.mark.skip(reason="not sure how to handle this")
def test_row_given_object_with_no_render_method():
    # How do I want to handle this?
    row = Row("just a string")

    playing_row = row.render


def test_grid_renders_4_rows():
    row_1 = Mock(render="row1")
    row_2 = Mock(render="row2")
    row_3 = Mock(render="row3")
    row_4 = Mock(render="row4")

    rows = [row_1, row_2, row_3, row_4]

    grid = Grid(rows)
    playing_grid = grid.render
    expected_playing_grid = "row1\nrow2\nrow3\nrow4"
    assert playing_grid == expected_playing_grid


def test_grid_everybody_move_human_moves_left():
    row_1 = Mock(render="row1", human_in_row=[])
    row_2 = Mock(render="row2", human_in_row=[1], move_left=Mock())
    row_3 = Mock(render="row3", human_in_row=[])
    row_4 = Mock(render="row4", human_in_row=[])

    rows = [row_1, row_2, row_3, row_4]

    grid = Grid(rows)
    grid.everybody_move()
    row_2.move_left.assert_called()


def test_initializes_with_grid_size():
    grid = Grid(size=[4, 4])
    assert grid.length == 4
    assert grid.width == 4


def test_add_human():
    mock_human = Mock()
    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    grid.add_human(mock_human, starting_coordinates)
    assert [1, 2] == grid.coordinates[mock_human]


def test_add_zombie():
    mock_zombie = Mock()
    starting_coordinates = [2, 2]
    grid = Grid(size=[4, 4])
    grid.add_zombie(mock_zombie, starting_coordinates)
    assert [2, 2] == grid.coordinates[mock_zombie]


def test_grid_everybody_move_human_moves_left():
    mock_human = Mock()
    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    grid.add_human(mock_human, starting_coordinates)

    grid.everybody_move()
    assert grid.coordinates[mock_human] == [0, 2]


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
