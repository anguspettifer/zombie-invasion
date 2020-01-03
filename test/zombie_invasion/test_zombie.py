import pytest
from mock import Mock, patch

from zombie_invasion.zombie import Zombie


def test_zombie_colour_default():
    zombie = Zombie()
    assert zombie.render == 'Z'


def test_zombie_move():
    """
    Given the coordinates of the nearest human, a zombie will move one square closer
    """
    zombie = Zombie()
    coordinates = [1, 2]
    human_coordinates = {Mock(): [1, 0]}

    assert zombie.move(coordinates, human_coordinates) == [1, 1]


def test_zombie_move_choice():
    """
    Given the coordinates of the 2 humans, a zombie will move one square closer to the nearest one
    """
    zombie = Zombie()
    coordinates = [1, 2]
    human_coordinates = {
        Mock(): [1, 3],
        Mock(): [1, 0]
    }

    assert zombie.move(coordinates, human_coordinates) == [1, 3]


@patch("zombie_invasion.zombie.random")
def test_zombie_move_random(random):
    #TODO: struggling to test randomness here. since the dictionary iteration changes order anyway so even stubbing out randint does nto guarantee a result
    """
    Given the coordinates of the 2 humans that are equidistance, a zombie will move one square closer to one at random
    """
    zombie = Zombie()
    coordinates = [1, 2]
    human_coordinates = {
        Mock(): [1, 4],
        Mock(): [1, 0]
    }

    random.randint.return_value = 0
    assert zombie.move(coordinates, human_coordinates) == [1, 3]


def test_zombie_move_memory():
    """
    A zombie moved towards a human on the previous go
    Now it is equidistance from 2 humans, one of which was the one it chased the previous go
    It will move towards the one it faced the previous go.
    """



@pytest.mark.parametrize("x, y, expected", [(4, 1, 3), (4, 2, 3), (2, 2, 2), (0, 3, 1)])
def test__move_one_closer(x, y, expected):
    """
    Given a square in a certain dimension, returns one square closer to another square
    """
    zombie = Zombie()
    assert zombie._move_one_closer(x, y) == expected


@patch("zombie_invasion.zombie.random")
def test__random_closest_human_coordinates(random):
    """
    Given human coordinates and their absolute distances
    Test returns random closest human
    """
    zombie = Zombie()
    coordinates = [1, 2]
    human_coordinates = {
        Mock(): [1, 4],
        Mock(): [1, 0]
    }
    random.randint.return_value = 0

    assert zombie._random_closest_human_coordinates(coordinates, human_coordinates) == [1, 4]