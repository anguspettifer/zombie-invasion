import time

from mock import patch, Mock, call
import pandas as pd

from zombie_invasion.game import Game
from zombie_invasion.grid import Grid
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


def set_up_game_with(mock_input, mock_print, dimensions=[4, 3], number_of_humans=5, number_of_zombies=3,
                     human_speed=1, grid_class=False):
    # Create helper function to decouple tests
    mock_input.side_effect = [dimensions[0], dimensions[1], number_of_humans, number_of_zombies, human_speed]
    game = Game()
    if grid_class:
        game.set_up(grid_class)
    else:
        game.set_up()
    return game


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_request_dimensions(mock_input, mock_print):
    """
    Check that requesting the user for dimensions as an input saves response
    """
    mock_input.side_effect = [20, 40]
    game = Game()
    game._request_dimensions()
    mock_print.assert_has_calls([
        call("Please enter width"),
        call("Please enter length")
    ])
    assert game.dimensions == (20, 40)


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_request_number_of_humans(mock_input, mock_print):
    """
    Check that requesting the user for number of humans as an input saves response
    """
    mock_input.return_value = 5
    game = Game()
    game._request_number_of_humans()
    mock_print.assert_called_with("Please enter number of humans")
    assert game.number_of_humans == 5


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_request_number_of_zombies(mock_input, mock_print):
    """
    Check that requesting the user for number of zombies as an input saves response
    """
    mock_input.return_value = 3
    game = Game()
    game._request_number_of_zombies()
    mock_print.assert_called_with("Please enter number of zombies")
    assert game.number_of_zombies == 3


@patch('zombie_invasion.game.random')
def test_add_humans(mock_random):
    """
    Set the number of humans that should be in the game
    Assert this this number are indeed added
    """
    mock_random.randint.side_effect = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

    game = Game()
    game.number_of_humans = 5
    game.grid = Mock(add_player=Mock())
    mock_human = Mock(side_effect=["h1", "h2", "h3", "h4", "h5"])

    game._add_humans(mock_human)

    game.grid.add_player.assert_has_calls([
        call("h1", [1, 1]),
        call("h2", [2, 2]),
        call("h3", [3, 3]),
        call("h4", [4, 4]),
        call("h5", [5, 5])
    ])


@patch('zombie_invasion.game.random')
def test_add_zombie(mock_random):
    #TODO: ask andy. Should I be testing the inability to add two zombies to the same square here?
    """
    Add two zombies to the grid
    Assert that add_player is called twice
    """
    mock_random.choice.side_effect = [1, 1, 2, 2]

    game = Game()
    game.number_of_zombies = 2

    grid = Mock(add_player=Mock(), unoccupied_coordinates=None)
    game.grid = grid

    game._add_zombies()

    assert grid.add_player.call_count == 2



## are these feature tests?

@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_creates_grid(mock_input, mock_print):
    """
    set up game creates a grid with dimensions
    """
    game = set_up_game_with(mock_input, mock_print)
    assert game.grid.width == 3
    assert game.grid.length == 2


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_creates_grid(mock_input, mock_print):
    """
    Bug fix dimensions as strings
    """
    dimensions = ["4", "3"]
    number_of_humans = "5"
    number_of_zombies = "3"
    game = set_up_game_with(mock_input, mock_print, dimensions, number_of_humans, number_of_zombies)
    assert game.grid.width == 3
    assert game.grid.length == 2
    assert len(game.grid.zombie_coordinates) == 3
    assert len(game.grid.human_coordinates) == 5


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
@patch('zombie_invasion.game.random')
def test_game_set_up_creates_grid(mock_random, mock_input, mock_print):
    """
    Bug fix.
    Create game with 2 zombies and no humans
    assert that 2 zombies are added
    """
    mock_random.choice.side_effect = [[1, 1], [2, 2]]

    dimensions = ["4", "3"]
    number_of_humans = "0"
    number_of_zombies = "2"
    human_speed = "3"

    mock_grid_class = Mock()
    mock_grid = Mock(add_player=Mock(), unoccupied_coordinates=None)
    mock_grid_class.return_value = mock_grid

    set_up_game_with(mock_input, mock_print, dimensions, number_of_humans, number_of_zombies, human_speed, mock_grid_class)

    assert mock_grid.add_player.call_count == 2


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_adds_humans_and_zombies(mock_input, mock_print):
    """
    Set up a game with dimensions
    Assert that grid stores the correc dimensions
    """
    game = set_up_game_with(mock_input, mock_print)

    assert game.grid.length == 2
    assert game.grid.width == 3


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_start_calls_human_move_until_there_are_no_humans(mock_input, mock_print):
    """
    Create a game with 1 human and 1 zombie
    Start the game
    Assert that at the end of the game there are 2 zombies and no humans
    """

    dimensions = [2, 2]
    number_of_humans = 1
    number_of_zombies = 1

    game = set_up_game_with(mock_input, mock_print, dimensions, number_of_humans, number_of_zombies)

    game.play()

    assert game.number_of_humans == 0
    assert game.number_of_zombies == 2


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_start_calls_human_move_until_there_are_no_humans(mock_input, mock_print):
    """
    Bug fix: Assert that end of game display is called with remaining number of humans and zombies
    """

    dimensions = [2, 2]
    number_of_humans = 0
    number_of_zombies = 1

    game = set_up_game_with(mock_input, mock_print, dimensions, number_of_humans, number_of_zombies)

    mock_display = Mock(end_game_display=Mock())
    mock_display_class = Mock(return_value=mock_display)
    game.play(mock_display_class)

    mock_display.end_game_display.assert_called_with(
        number_of_humans, number_of_zombies, 0
    )


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_errors_if_there_is_not_enough_room_for_all_zombies(mock_input, mock_print):
    """
    Create a game 2 x 2 game
    Attempt to add 5 zombies
    Expect standard out to print error and print the actual number of zombies added
    Expect number of zombies to be 4
    """

    dimensions = [2, 2]
    number_of_humans = 0
    number_of_zombies = 5

    game = set_up_game_with(mock_input, mock_print, dimensions, number_of_humans, number_of_zombies)

    mock_print.assert_any_call(f"You have reached your zombie limit, 4 zombies added")
    assert game.number_of_zombies == 4


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_keeps_track_of_number_of_turns(mock_input, mock_print):
    """
    Create a game 2x2 game with 1 zombie and 3 humans
    Start the game
    Assert that at the end of the game the number of turns is 2
    """
    dimensions = [2, 2]
    number_of_humans = 2
    number_of_zombies = 1

    game = set_up_game_with(mock_input, mock_print, dimensions, number_of_humans, number_of_zombies)

    game.play()

    assert game.number_of_turns == 2


@patch('zombie_invasion.display.input')
@patch('zombie_invasion.display.print')
def test_display_initial_display(mock_print, mock_input):
    """
    Create a game object with grid dimensions
    Expect initial_display to be called on the display object
    """
    # TODO: Question for Andy, what is a sensible way to test this method? This test is essentially replicated

    mock_input.return_value = None

    width = 3
    length = 3

    game = Game()
    game.grid = Mock(width=width, length=length)

    empty_row = ["." for i in range(width + 1)]
    df = pd.DataFrame(data=[empty_row for i in range(length + 1)])

    game.initial_display()
    mock_print.assert_called_with(f"Please adjust screen to the size of the below grid:\n{df}\nplease hit enter")


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_records_number_of_players(mock_input, mock_print):
    """
    Create a 2X2 game
    Add 1 zombie and 1 human
    Set both sets of coordinates to the same square
    Check that the number of players is recorded after the move
    """
    dimensions = [2, 2]
    number_of_humans = 1
    number_of_zombies = 1

    game = set_up_game_with(mock_input, mock_print, dimensions, number_of_humans, number_of_zombies)

    for player in game.grid.players_and_coordinates:
        game.grid.players_and_coordinates[player] = [1, 1]
    game.grid.convert_if_needed()
    game._update_number_of_players()

    assert game.number_of_zombies == 2
    assert game.number_of_humans == 0


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_request_human_speed(mock_input, mock_print):
    """
    Mock input value
    Call request_human_speed
    Assert that human_speed has been set
    """
    mock_input.return_value = 3
    game = Game()
    game._request_human_speed()
    assert game.human_speed == 3
