from mock import patch

from zombie_invasion.game import Game


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
def test_game_request_dimensions(mock_input, mock_print):
    """
    Check that requesting the user for number of humans as an input saves response
    """
    mock_input.return_value = 5
    game = Game()
    game._request_number_of_humans()
    mock_print.assert_called_with("Please enter number of humans")
    assert game.number_of_humans == 5
