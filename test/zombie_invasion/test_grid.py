import pytest

from zombie_invasion.grid import Grid
from mock import Mock


def test_initializes_with_grid_size():
    grid = Grid(size=[4, 4])
    assert grid.length == 4
    assert grid.width == 4


def test_add_human():
    mock_human = Mock(render='H')
    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_human, starting_coordinates)
    assert [1, 2] == grid.human_coordinates[mock_human]


def test_add_zombie():
    mock_zombie = Mock(render='Z')
    starting_coordinates = [1, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_zombie, starting_coordinates)
    assert [1, 2] == grid.zombie_coordinates[mock_zombie]


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
    mock_human = Mock(render='Z')
    mock_zombie = Mock(render="H")
    coordinates = [2, 2]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_human, coordinates)
    grid.add_player(mock_zombie, coordinates)

    grid.convert_if_needed()
    assert len(grid.zombie_coordinates) == 2


def test_convert_if_needed_more_than_one_convert():
    """
    Create a grid with 3 humans and 3 zombies, each pair with the same coordinates
    Assert that each human turns into a zombie
    """
    mock_human_1 = Mock(render='Z')
    mock_zombie_1 = Mock(render="H")
    coordinates_1 = [2, 2]
    mock_human_2 = Mock(render='Z')
    mock_zombie_2 = Mock(render="H")
    coordinates_2 = [3, 3]
    mock_human_3 = Mock(render='Z')
    mock_zombie_3 = Mock(render="H")
    coordinates_3 = [1, 1]
    grid = Grid(size=[4, 4])
    grid.add_player(mock_human_1, coordinates_1)
    grid.add_player(mock_zombie_1, coordinates_1)
    grid.add_player(mock_human_2, coordinates_2)
    grid.add_player(mock_zombie_2, coordinates_2)
    grid.add_player(mock_human_3, coordinates_3)
    grid.add_player(mock_zombie_3, coordinates_3)

    grid.convert_if_needed()
    assert len(grid.zombie_coordinates) == 6

