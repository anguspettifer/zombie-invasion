from mock import Mock, call, patch

from play_game import play_game


class MockGame:
    def __init__(self):
        self.set_up = Mock()
        self.initial_display = Mock()
        self.play = Mock()


def test_play_game():
    """
    test play game calls game methods in the right order
    """
    mock_game = MockGame()
    play_game(mock_game)
    mock_game.set_up.assert_called_once()
    mock_game.initial_display.assert_called_once()
    mock_game.play.assert_called_once()
