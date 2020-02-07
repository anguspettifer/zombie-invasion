import pytest
from mock import Mock, patch

from zombie_invasion.human import Human
from zombie_invasion.zombie import Zombie

# TODO: ASK ANDY. I changed all the mock humans to actual humans in order to pass line 60. Does this increase coupling?
def test_zombie_colour_default():
    zombie = Zombie()
    assert zombie.render == 'Z'


def test_zombie_move():
    """
    Given the coordinates of the nearest human, a zombie will move one square closer
    """
    zombie = Zombie()
    coordinates = [1, 2]
    players_and_coordinates = {Human(): [1, 0]}

    assert zombie.move(coordinates, None, players_and_coordinates) == [1, 1]


def test_zombie_move_choice():
    """
    Given the coordinates of the 2 humans, a zombie will move one square closer to the nearest one
    """
    zombie = Zombie()
    coordinates = [1, 2]
    human_coordinates = {
        Human(): [1, 3],
        Human(): [1, 0]
    }

    assert zombie.move(coordinates, None, human_coordinates) == [1, 3]


def side_effect(list_):
    return list_[0]

@patch("zombie_invasion.zombie.random")
def test_zombie_move_random(random):
    """
    Given the coordinates of the 2 humans that are equidistance, a zombie will move one square closer to one at random
    """
    zombie = Zombie()
    coordinates = [1, 2]
    human_coordinates = {
        Human(): [1, 4],
        Human(): [1, 0]
    }

    random.choice.side_effect = side_effect
    assert zombie.move(coordinates, None, human_coordinates) == [1, 3]


@patch("zombie_invasion.zombie.random")
def test_zombie_move_memory(random):
    """
    A zombie moved towards a human on the previous go
    Now it is equidistant from 2 humans, one of which was the one it chased the previous go
    It will move towards the one it faced the previous go.
    """
    zombie = Zombie()
    coordinates = [1, 1]
    mock_human_1 = Human()
    mock_human_2 = Human()

    human_coordinates_1 = {
        mock_human_1: [3, 1],
        mock_human_2: [3, 3]
    }

    human_coordinates_2 = {
        mock_human_1: [3, 1],
        mock_human_2: [2, 2]
    }

    random.choice.side_effect = side_effect
    new_coordinates = zombie.move(coordinates, None, human_coordinates_1)
    assert zombie.move(new_coordinates, None, human_coordinates_2) == [3, 1]


@pytest.mark.parametrize("x, y, expected", [(4, 1, 3), (4, 2, 3), (2, 2, 2), (0, 3, 1)])
def test__move_one_closer(x, y, expected):
    """
    Given a square in a certain dimension, returns one square closer to another square
    """
    zombie = Zombie()
    assert zombie._move_one_closer(x, y) == expected


def test__random_closest_human_coordinates():
    """
    Given 2 humans equidistant and one further away
    Test returns random the two closest
    """
    zombie = Zombie()
    coordinates = [1, 2]
    human_1 = Human()
    human_2 = Human()
    human_3 = Human()

    human_coordinates = {
        human_1: [1, 4],
        human_2: [1, 0],
        human_3: [0, 0]
    }

    assert zombie._closest_human_coordinates(coordinates, human_coordinates) == {
        human_1: [1, 4],
        human_2: [1, 0]
    }
