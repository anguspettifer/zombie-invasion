from zombie_invasion.grid import Grid, BlankSquare, Row
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


def test_grid_renders_with_zombie_and_human():
    # Given the means to start the program
    # When the user initiates the start
    # Then the human and zombie are on different squares
    starter_square = "O"
    zombie = Zombie()
    human = Human()
    squares = [BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)]
    top_row = Row([zombie, BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)])
    bottom_row = Row([human, BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)])

    rows = [top_row, Row(squares), Row(squares), bottom_row]

    grid = Grid(rows)
    assert grid.render == "ZOOO\n" \
                          "OOOO\n" \
                          "OOOO\n" \
                          "HOOO"




"""
As a viewer
I can watch a human move in a random
So that I can be amused**
"""


def test_human_moves_one_space():
    # Given a program in progress
    # When it is time for a new go or turn
    # Then the human will move 1 pace in a random direction (N, NE, E, SE, S, SW, W, NW)
    starter_square = "O"
    human = Human()
    squares = [BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square), BlankSquare(starter_square)]
    second_row = Row([BlankSquare(starter_square), human, BlankSquare(starter_square), BlankSquare(starter_square)])

    rows = [Row(squares), second_row, Row(squares), Row(squares)]

    grid = Grid(rows)

    grid.everybody_move()

    possible_move_options = [
        "HOOO\nOOOO\nOOOO\nOOOO",
        "OHOO\nOOOO\nOOOO\nOOOO",
        "OOHO\nOOOO\nOOOO\nOOOO",
        "OOOO\nHOOO\nOOOO\nOOOO",
        "OOOO\nOOHO\nOOOO\nOOOO",
        "OOOO\nOOOO\nHOOO\nOOOO",
        "OOOO\nOOOO\nOHOO\nOOOO",
        "OOOO\nOOOO\nOOHO\nOOOO",
    ]

    assert grid.render in possible_move_options



def test_human_does_not_move_if_wall():
    # Given a program in progress
    # When a human moves into a wall
    # Then the human will not move on that go
    return

