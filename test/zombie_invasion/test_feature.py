from zombie_invasion.grid import Grid, BlankSquare, Row
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


def test_grid_renders():
    # Given the means to start the program
    # When the user initiates the start
    # Then a 4x4 grid is rendered on the screen

    starter_square = "O"
    squares = [BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)]
    rows = [Row(squares), Row(squares), Row(squares), Row(squares)]

    grid = Grid(rows)
    assert grid.render == "OOOO\n" \
                          "OOOO\n" \
                          "OOOO\n" \
                          "OOOO"


def test_grid_renders_with_human():
    # Given the means to start the program
    # When the user initiates the start
    # Then a human is occupying a single square

    starter_square = "O"
    human = Human()
    squares = [BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)]
    top_row = Row([human, BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)])

    rows = [top_row, Row(squares), Row(squares), Row(squares)]

    grid = Grid(rows)
    assert grid.render == "HOOO\n" \
                          "OOOO\n" \
                          "OOOO\n" \
                          "OOOO"

def test_grid_renders_with_zombie():
    # Given the means to start the program
    # When the user initiates the start
    # Then a zombie is occupying a single square

    starter_square = "O"
    zombie = Zombie()
    squares = [BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)]
    top_row = Row([zombie, BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)])

    rows = [top_row, Row(squares), Row(squares), Row(squares)]

    grid = Grid(rows)
    assert grid.render == "ZOOO\n" \
                          "OOOO\n" \
                          "OOOO\n" \
                          "OOOO"
