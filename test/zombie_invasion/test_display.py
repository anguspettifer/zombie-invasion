import pandas as pd
from mock import Mock, patch, call
from pandas.util.testing import assert_frame_equal

from zombie_invasion.display import Display
from zombie_invasion.grid import Grid
from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


def set_up_grid():
    grid = Grid([4, 4])
    grid.players_and_coordinates[Human()] = [0, 0]
    grid.players_and_coordinates[Zombie()] = [1, 1]

    return grid

    # TODO: Ask andy. Again, we are better off instansiating a real grid rather than random mocks in order to decouple


def test_display_human_and_zombie_in_grid():
    """
    Set up display with 1 human and 1 zombie
    Assert the expected display
    """
    top_row = ["H", ".", ".", "."]
    second_row = [".", "Z", ".", "."]
    row = [".", ".", ".", "."]

    expected_df = pd.DataFrame([top_row, second_row, row, row])
    grid = set_up_grid()
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

    grid = set_up_grid()

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

    grid = set_up_grid()

    display = Display(grid)
    df = display.render()
    number_of_humans = 1
    number_of_zombies = 1
    number_of_turns = 3

    display.end_game_display(number_of_humans, number_of_zombies, number_of_turns)

    mock_print.assert_called_with(
        f"Human count: {number_of_humans}\nZombie count: {number_of_zombies}\n{df}\nNumber of turns: {number_of_turns}"
        f"\nHumans extinct!")
