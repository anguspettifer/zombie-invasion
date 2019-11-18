from zombie_invasion.grid import Grid, Square, Row
from zombie_invasion.human import Human


def test_grid_renders():
    # Given the means to start the program
    # When the user initiates the start
    # Then a 4x4 grid is rendered on the screen

    starter_square = "O"
    squares = [Square(starter_square), Square(starter_square), Square(starter_square), Square(starter_square)]
    rows = [Row(squares), Row(squares), Row(squares), Row(squares)]

    grid = Grid(rows)
    grid.render = "OOOO\n" \
                  "OOOO\n" \
                  "OOOO\n" \
                  "OOOO"


def test_grid_renders_with_human():
    # Given the means to start the program
    # When the user initiates the start
    # Then a human is occupying a single square

    starter_square = "O"
    human = Human()
    squares = [Square(human), Square(starter_square), Square(starter_square), Square(starter_square)]
    top_row = Row([Square(starter_square), Square(starter_square), Square(starter_square), Square(starter_square)])

    rows = [top_row, Row(squares), Row(squares), Row(squares)]

    grid = Grid(rows)
    grid.render = "HOOO\n" \
                  "OOOO\n" \
                  "OOOO\n" \
                  "OOOO"