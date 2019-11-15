from zombie_invasion.grid import Grid, Square, Row


def test_grid_renders():
    # Given the means to start the program
    # When the user initiates the start
    # Then a 4x4 grid is rendered on the screen

    starter_square = "|_|"
    squares = [Square(starter_square), Square(starter_square), Square(starter_square), Square(starter_square)]
    rows = [Row(squares), Row(squares), Row(squares), Row(squares)]

    grid = Grid(rows)
    grid.render = "|_||_||_||_|\n" \
                  "|_||_||_||_|\n" \
                  "|_||_||_||_|\n" \
                  "|_||_||_||_|"
