import pytest
from mock import Mock

from zombie_invasion.zombie import Zombie


def test_zombie_colour_default():
    zombie = Zombie()
    assert zombie.render == 'Z'


def test_zombie_move():
    zombie = Zombie()
    coordinates = [1, 2]
    human_coordinates = {Mock(): [1, 0]}

    assert zombie.move(coordinates, human_coordinates) == [1, 1]


@pytest.mark.parametrize("x, y, expected", [(4, 1, 3), (4, 2, 3), (2, 2, 2), (0, 3, 1)])
def test__move_one_closer(x, y, expected):
    """
    Given a square in a certain dimension, returns one square closer to another square
    """
    zombie = Zombie()
    assert zombie._move_one_closer(x, y) == expected
