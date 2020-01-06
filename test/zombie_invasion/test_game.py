from mock import patch

from zombie_invasion.game import Game


@patch('zombie_invasion.game.print')
@patch('zombie_invasion.game.input')
def test_game_request_dimensions(mock_input, mock_print):
    """
    Check that starting a game asks the user for dimensions as an input and saves response
    """
    mock_input.return_value = (20, 40)
    game = Game()
    game.start()
    mock_print.assert_called_with("Please enter dimensions")
    assert game.dimensions == (20, 40)
