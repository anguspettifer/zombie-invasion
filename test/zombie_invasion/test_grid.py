import pytest

from zombie_invasion.grid import Grid, Square, Row
from mock import Mock


def test_square_renders_empty_by_default():
    starter_square = "|_|"
    square = Square(starter_square)
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
