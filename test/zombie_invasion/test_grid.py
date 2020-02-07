import pytest

from zombie_invasion.grid import Grid
from mock import Mock

from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie


def test_initializes_with_grid_size():
    grid = Grid(size=[4, 4])
    assert grid.length == 3
    assert grid.width == 3


def test_add_human():
    """
    Add human to the grid
    Check that the are stored
    """
    mock_human = Mock(render='H')
    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_human, starting_coordinates)
    assert [1, 2] == grid.players_and_coordinates[mock_human]


def test_add_human_off_grid():
    """
    A player should not be able to be added out of bounds
    """
    mock_human = Mock()
    starting_coordinates = [5, 5]
    grid = Grid(size=[4, 4])
    with pytest.raises(ValueError):
        grid.add_player(mock_human, starting_coordinates)


def test_convert_if_needed():
    """
    Create a grid with a human and a zombie with the same coordinates
    Assert that the human turns into a zombie
    """
    mock_human = Mock(render='Z')
    mock_zombie = Mock(render="H")
    coordinates = [2, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_human, coordinates)
    grid.add_player(mock_zombie, coordinates)

    grid.convert_if_needed()
    assert len(grid.zombie_coordinates) == 2


def test_convert_if_needed():
    """
    Create a grid with a human and a zombie with the same coordinates
    Assert that the human turns into a zombie
    """

    coordinates = [2, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(Human(), coordinates)
    grid.add_player(Zombie(), coordinates)

    grid.convert_if_needed()
    players = grid.players_and_coordinates.keys()
    assert len([x for x in players if type(x) == Zombie]) == 2


def test_convert_if_needed_more_than_one_convert():
    """
    Create a grid with 3 humans and 3 zombies, each pair with the same coordinates
    Assert that each human turns into a zombie
    """

    coordinates_1 = [2, 2]
    coordinates_2 = [3, 3]
    coordinates_3 = [1, 1]

    grid = Grid(size=[4, 4])

    grid.add_player(Human(), coordinates_1)
    grid.add_player(Zombie(), coordinates_1)
    grid.add_player(Human(), coordinates_2)
    grid.add_player(Zombie(), coordinates_2)
    grid.add_player(Human(), coordinates_3)
    grid.add_player(Zombie(), coordinates_3)

    grid.convert_if_needed()
    players = grid.players_and_coordinates.keys()
    assert len([x for x in players if type(x) == Zombie]) == 6


def test_convert_if_needed_nothing_to_convert():
    """
    If 2 zombies and a human are on the same square
    The human becomes a zombie
    """
    grid = Grid(size=[4, 4])
    grid.add_player(Human(), [2, 2])
    grid.add_player(Zombie(), [2, 2])
    grid.add_player(Zombie(), [2, 2])
    grid.convert_if_needed()

    players = grid.players_and_coordinates.keys()
    assert len([x for x in players if type(x) == Human]) == 0
    assert len([x for x in players if type(x) == Zombie]) == 3


def test_convert_if_needed_converts_one():
    """
    If 1 zombie and a 2 humans are on the same square
    One human becomes a zombie, the other doesn't
    """
    grid = Grid(size=[4, 4])
    grid.add_player(Human(), [2, 2])
    grid.add_player(Human(), [2, 2])
    grid.add_player(Zombie(), [2, 2])
    grid.convert_if_needed()

    players = grid.players_and_coordinates.keys()
    assert len([x for x in players if type(x) == Human]) == 1
    assert len([x for x in players if type(x) == Zombie]) == 2


def test_convert_if_needed_converts_two():
    """
    If 2 zombies and a 2 humans are on the same square
    Both humans become zombies
    """
    grid = Grid(size=[4, 4])
    grid.add_player(Human(), [2, 2])
    grid.add_player(Human(), [2, 2])
    grid.add_player(Zombie(), [2, 2])
    grid.add_player(Zombie(), [2, 2])
    grid.convert_if_needed()

    players = grid.players_and_coordinates.keys()
    assert len([x for x in players if type(x) == Human]) == 0
    assert len([x for x in players if type(x) == Zombie]) == 4


def test_add_player_removes_coordinates_from_blank_square_coordinates():
    """
    Create a grid 4 x 4
    Add a zombie at 0, 0
    Add a human at 0, 1
    Assert both have been removed from blank_square_coordinates
    Assert total number of blank squares has been reduced by 2
    """
    grid = Grid([4, 4])
    grid.add_player(Mock(render="H"), [0, 0])
    grid.add_player(Mock(render="Z"), [0, 1])
    assert [0, 0] not in grid.unoccupied_coordinates
    assert [0, 1] not in grid.unoccupied_coordinates
    assert len(grid.unoccupied_coordinates) == 14


def test_add_player_adds_two_humans_to_same_square():
    """
    Bug fix - code should not error in this scenario
    Create 4x4 grid
    Add 2 humans on the same square [0, 0]
    Assert that unoccupied_coordinates does not include [0, 0]
    """
    grid = Grid([4, 4])
    grid.add_player(Mock(render="H"), [0, 0])
    grid.add_player(Mock(render="H"), [0, 0])
    assert [0, 0] not in grid.unoccupied_coordinates


def test_unoccupied_coordinates_not_settable():
    """
    In order to maintain a single source of truth
        unoccupied_coordinates can only be changed when the players_and_coordinates is changed
    Set up grid
    Change the unnocupied_coordinates attribute
    Assert an error is raised
    """
    grid = Grid([4, 4])
    with pytest.raises(AttributeError):
        grid.unoccupied_coordinates = [1, 1]
