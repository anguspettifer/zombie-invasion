import pandas as pd
from mock import Mock, patch, call
from pandas.util.testing import assert_frame_equal

from zombie_invasion.display import Display


def test_display_empty_grid():
    row = [".", ".", ".", "."]
    expected_df = pd.DataFrame([row, row, row, row])

    grid = Mock(width=3, length=3, human_coordinates={}, zombie_coordinates={})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_human_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "H", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_human = Mock(render="H")
    grid = Mock(width=3, length=3, human_coordinates={mock_human: [1, 1]}, zombie_coordinates={})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_zombie_in_grid():
    row = [".", ".", ".", "."]
    second_row = [".", "Z", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_zombie = Mock(render="Z")
    grid = Mock(width=3, length=3, human_coordinates={}, zombie_coordinates={mock_zombie: [1, 1]})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


def test_display_no_humans():
    row = [".", ".", ".", "."]
    second_row = [".", "Z", ".", "."]
    expected_df = pd.DataFrame([row, second_row, row, row])

    mock_zombie = Mock(render="Z")
    grid = Mock(width=3, length=3, human_coordinates={}, zombie_coordinates={mock_zombie: [1, 1]})
    display = Display(grid)

    assert_frame_equal(display.render(), expected_df)


@patch('zombie_invasion.display.print')
@patch('zombie_invasion.display.input')
def test_display_inital_display(mock_input, mock_print):
    """
    Create display object and assert intial display is as expected
    """

    mock_input.return_value = None

    width = 3
    length = 3

    grid = Mock(width=width, length=length)
    display = Display(grid)
    display.initial_display()

    empty_row = ["." for i in range(width + 1)]
    df = pd.DataFrame(data=[empty_row for i in range(length + 1)])

    display.initial_display()
    mock_print.assert_called_with(f"Please adjust screen to the size of the below grid:\n{df}\nplease hit enter")


@patch('zombie_invasion.display.print')
@patch('zombie_invasion.display.input')
def test_display_game_display(mock_input, mock_print):
    """
    Create display object and assert during game display is as expected
    """
    mock_input.return_value = None

    width = 3
    length = 3
    human = Mock(render="H")
    zombie = Mock(render="Z")
    grid = Mock(width=width, length=length, human_coordinates={human: [1, 1]}, zombie_coordinates={zombie: [2, 1]})

    display = Display(grid)
    df = display.render()
    number_of_humans = 1
    number_of_zombies = 1

    display.game_display(number_of_humans, number_of_zombies)

    mock_print.assert_called_with(f"Human count: {number_of_humans} \nZombie count: {number_of_zombies} \n {df}")


@patch('zombie_invasion.display.print')
@patch('zombie_invasion.display.input')
def test_end_game_display(mock_input, mock_print):
    """
    Create display object and assert end game display is as expected
    """
    mock_input.return_value = None

    width = 3
    length = 3
    human = Mock(render="H")
    zombie = Mock(render="Z")
    grid = Mock(width=width, length=length, human_coordinates={human: [1, 1]}, zombie_coordinates={zombie: [2, 1]})

    display = Display(grid)
    df = display.render()
    number_of_humans = 1
    number_of_zombies = 1
    number_of_turns = 3

    display.end_game_display(number_of_humans, number_of_zombies, number_of_turns)

    mock_print.assert_called_with(
        f"Human count: {number_of_humans}\nZombie count: {number_of_zombies}\n{df}\nNumber of turns: {number_of_turns}"
        f"\nHumans extinct!")
