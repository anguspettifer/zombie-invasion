from mock import patch

from zombie_invasion.human import Human


def test_human_colour_default():
    human = Human()
    assert human.render == 'H'


def test_move():
    """
    A human does not know it's coordinates.
    But if it is passed it's coordinates and the grid dimensions it knows how to move
    """
    human = Human()
    coordinates = [2, 1]
    dimensions = [3, 4]

    new_coordinates = human.move(coordinates, dimensions)

    possible_new_coordinates = [[2, 0], [3, 0], [3, 1], [3, 2], [2, 2], [1, 2], [1, 1], [1, 0]]

    assert new_coordinates in possible_new_coordinates


@patch("zombie_invasion.human.random")
def test_human_cannot_move_through_grid_wall(mock_random):
    """
    If a human tries to move through a wall it must remain where it was in that dimension
    """
    mock_random.randint.return_value = 0
    human = Human()

    coordinates = [0, 0]
    dimensions = [4, 4]

    new_coordinates = human.move(coordinates, dimensions)
    assert new_coordinates == [0, 0]


@patch("zombie_invasion.human.random")
def test_human_moves_number_of_squares_according_to_speed(mock_random):
    """
    Instansiate a human with a speed = 3
    Give it coordinates of 0, 0 in a grid of 3 x 3
    Mock random so that the human will move to the right along the x axis
    Call move
    Assert that the human is at 3, 0
    """
    mock_random.randint.return_value = 6
    human = Human(speed=3)
    coordinates = [0, 0]
    grid_dimensions = [3, 3]
    assert human.move(coordinates, grid_dimensions) == [3, 0]


