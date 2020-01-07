from mock import patch, Mock, call

from zombie_invasion.game import Game
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_request_dimensions(mock_input, mock_print):
    """
    Check that requesting the user for dimensions as an input saves response
    """
    mock_input.return_value = (20, 40)
    game = Game()
    game._request_dimensions()
    mock_print.assert_called_with("Please enter dimensions")
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
        call("h1", (1, 1)),
        call("h2", (2, 2)),
        call("h3", (3, 3)),
        call("h4", (4, 4)),
        call("h5", (5, 5))
    ])


## are these feature tests?

@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_creates_grid(mock_input, mock_print):
    """
    set up game creates a grid with dimensions
    """
    mock_input.side_effect = [(4, 3), 5, 3]
    game = Game()
    game.set_up()
    assert game.grid.width == 4
    assert game.grid.length == 3


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_set_up_adds_humans_and_zombies(mock_input, mock_print):
    """
    set up game creates a grid with dimensions
    """
    mock_input.side_effect = [(4, 3), 5, 3]
    game = Game()
    game.set_up()

    humans = game.grid.human_coordinates.keys()
    assert all(isinstance(x, Human) for x in humans)

    zombies = game.grid.zombie_coordinates.keys()
    assert all(isinstance(x, Zombie) for x in zombies)


