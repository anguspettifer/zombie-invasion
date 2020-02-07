import pandas as pd
from mock import patch, call
from pandas.util.testing import assert_frame_equal

from zombie_invasion.game import Game
from zombie_invasion.grid import Grid
from zombie_invasion.display import Display
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
    grid.players_move()
    display = Display(grid)
    rendered_display = display.render()

    possible_human_coordinates = [[2, 0], [3, 0], [3, 1], [3, 2], [2, 2], [1, 2], [1, 1], [1, 0]]
    result = []
    for coordinates in possible_human_coordinates:
        result.append(rendered_display[coordinates[0]].loc[coordinates[1]])
    assert "H" in result


@patch("zombie_invasion.human.random")
def test_human_does_not_move_if_wall(mock_random):
    # Given a program in progress
    # When a human moves into a wall
    # Then the human will not move on that go
    mock_random.randint.return_value = 0
    human = Human()
    grid = Grid(size=[4, 3])
    grid.add_player(human, [0, 0])
    grid.players_move()
    display = Display(grid)
    rendered_display = display.render()
    assert rendered_display[0].loc[0] == "H"


"""
As a viewer
I can watch a zombie move towards the human
So that my desire for human demolition by zombies can be incited
"""


@patch("zombie_invasion.human.Human.move")
def test_zombie_moves_towards_human(mock_move):
    # Given a program in progress
    # When it is time for a new go or turn
    # Then the zombie will move 1 pace towards the human
    """
    Set up the game with Human on 0, 0 and zombie on 0, 2
    Ensure that human will not move on their go
    Call players-move()
    Assert that zombie is at 0, 1
    """
    mock_move.return_value = [0, 0]

    human = Human()
    zombie = Zombie()
    grid = Grid(size=[4, 3])
    grid.add_player(human, [0, 0])
    grid.add_player(zombie, [0, 2])
    grid.players_move()
    display = Display(grid)
    rendered_display = display.render()

    assert rendered_display[0].loc[1] == "Z"


"""
As a viewer
I can watch a zombie catch the human and turn it into a zombie
So that my desire for human demolition by zombies can be satisfied
"""


def test_zombie_turns_human_into_zombie():
    # Given a program in progress
    # When a zombie occupies the same square as the human
    # Then the human will become a zombie
    human = Human()
    zombie = Zombie()
    grid = Grid(size=[4, 3])
    grid.add_player(human, [0, 0])
    grid.add_player(zombie, [0, 0])
    grid.convert_if_needed()
    zombies = [x for x in grid.players_and_coordinates.keys() if type(x) == Zombie]
    assert len(zombies) == 2


"""As a viewer
I can trigger the start of the game
So that I can watch the mayhem unfold
"""


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_inputs(mock_input, mock_print):
    # Given a terminal in the correct directory
    # When I trigger the start of the game
    # Then I will be asked for:
    #     - dimensions
    #     - number of humans
    #     - number of zombies
    mock_input.side_effect = [4, 3, 5, 3]
    game = Game()
    game.set_up()
    mock_print.assert_has_calls([
        call("Please enter width"),
        call("Please enter length"),
        call("Please enter number of humans"),
        call("Please enter number of zombies")])


@patch('zombie_invasion.game.input')
def test_game_plays(mock_input):
    # Given I have triggered the start of the game
    # Once I have input the paramaters
    # Then the game will play out on my screen
    mock_input.side_effect = [10, 10, 5, 3]
    game = Game()
    game.set_up()
    game.play()
    assert game.number_of_humans == 0
    assert game.number_of_zombies == 8
