import time

from mock import patch, Mock, call
import pandas as pd

from zombie_invasion.game import Game
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


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
def test_add_players(mock_random):
    """
    Set the number of humans that should be in the game
    Assert this this number are indeed added
    """
    mock_random.randint.side_effect = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

    game = Game()
    game.number_of_humans = 5
    game.grid = Mock(add_player=Mock())
    mock_human = Mock(side_effect=["h1", "h2", "h3", "h4", "h5"])

    game._add_players(mock_human, game.number_of_humans)

    game.grid.add_player.assert_has_calls([
        call("h1", [1, 1]),
        call("h2", [2, 2]),
        call("h3", [3, 3]),
        call("h4", [4, 4]),
        call("h5", [5, 5])
    ])

## are these feature tests?

@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_creates_grid(mock_input, mock_print):
    """
    set up game creates a grid with dimensions
    """
    mock_input.side_effect = [4, 3, 5, 3]
    game = Game()
    game.set_up()
    assert game.grid.width == 3
    assert game.grid.length == 2


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_creates_grid(mock_input, mock_print):
    """
    Bug fix dimensions as strings
    """
    mock_input.side_effect = ["4", "3", "5", "3"]
    game = Game()
    game.set_up()
    assert game.grid.width == 3
    assert game.grid.length == 2
    assert len(game.grid.zombie_coordinates) == 3
    assert len(game.grid.human_coordinates) == 5


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_adds_humans_and_zombies(mock_input, mock_print):
    """
    set up game creates a grid with dimensions
    """
    mock_input.side_effect = [4, 3, 5, 3]
    game = Game()
    game.set_up()

    humans = game.grid.human_coordinates.keys()
    assert all(isinstance(x, Human) for x in humans)

    zombies = game.grid.zombie_coordinates.keys()
    assert all(isinstance(x, Zombie) for x in zombies)

@patch('zombie_invasion.game.input')
def test_game_start_calls_human_move_until_there_are_no_humans(mock_input):
    """
    Create a game with 1 human and 1 zombie
    Start the game
    Assert that at the end of the game there are 2 zombies and no humans
    """
    mock_input.side_effect = [4, 3, 1, 1]
    game = Game()
    game.set_up()

    game.play()

    assert len(game.grid.human_coordinates) == 0
    assert len(game.grid.zombie_coordinates) == 2


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_keeps_track_of_number_of_turns(mock_input, mock_print):
    """
    Create a game 1x1 game with 1 zombie and 7 humans
    Start the game
    Assert that at the end of the game the number of turns is 3
    """
    mock_input.side_effect = [1, 1, 7, 1]
    game = Game()
    game.set_up()

    game.play()

    assert game.number_of_turns == 3


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
