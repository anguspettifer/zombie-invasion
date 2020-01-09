import pytest

from zombie_invasion.grid import Grid, Conversion
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


def test_convert_if_needed_nothing_to_convert():
    """
    If 2 zombies and a human are on the same square
    The human becomes a zombie
    """
    grid = Grid(size=[4, 4])
    grid.add_player(Mock(render="H"), [2, 2])
    grid.add_player(Mock(render="Z"), [2, 2])
    grid.add_player(Mock(render="Z"), [2, 2])
    grid.convert_if_needed()
    assert len(grid.human_coordinates) == 0
    assert len(grid.zombie_coordinates) == 3

#TODO: test other iterations of humans zombies on same square
def test_convert_if_needed_nothing_to_convert():
    """
    If 1 zombie and a 2 humans are on the same square
    One human becomes a zombie, the other doesn't
    """
    grid = Grid(size=[4, 4])
    grid.add_player(Mock(render="H"), [2, 2])
    grid.add_player(Mock(render="H"), [2, 2])
    grid.add_player(Mock(render="Z"), [2, 2])
    grid.convert_if_needed()
    assert len(grid.human_coordinates) == 1
    assert len(grid.zombie_coordinates) == 2


def test_convert_if_needed_nothing_to_convert():
    """
    If 2 zombies and a 2 humans are on the same square
    Both humans become zombies
    """
    grid = Grid(size=[4, 4])
    grid.add_player(Mock(render="H"), [2, 2])
    grid.add_player(Mock(render="H"), [2, 2])
    grid.add_player(Mock(render="Z"), [2, 2])
    grid.add_player(Mock(render="Z"), [2, 2])
    grid.convert_if_needed()
    assert len(grid.human_coordinates) == 0
    assert len(grid.zombie_coordinates) == 4


class MockSource:
    identifyer="source"


class MockDestination:
    identifyer="destination"


def test_conversion():
    """
    Given source and destination objects with matching criteria
    Source object becomes destination object
    """

    conversion = Conversion(
        source_items={MockSource(): "A"},
        destination_items={MockDestination(): "A"},
        source_object=MockSource,
        destination_object=MockDestination
    )
    conversion.convert()
    assert len(conversion.destination_items) == 2
    for key in conversion.destination_items.keys():
        assert key.identifyer == "destination"


def test_conversion_2_source_1_destination():
    """
    Given 2 source and 1 destination objects with matching criteria
    1 source becomes a destination
    1 source is left as a source
    """

    conversion = Conversion(
        source_items={MockSource(): "A", MockSource(): "A"},
        destination_items={MockDestination(): "A"},
        source_object=MockSource,
        destination_object=MockDestination
    )
    conversion.convert()
    assert len(conversion.destination_items) == 2
    assert len(conversion.source_items) == 1


def test_conversion_1_source_2_destination():
    """
    Given 1 source and 2 destination objects with matching criteria
    the source becomes a destination
    """

    conversion = Conversion(
        source_items={MockSource(): "A"},
        destination_items={MockDestination(): "A", MockDestination(): "A"},
        source_object=MockSource,
        destination_object=MockDestination
    )
    conversion.convert()
    assert len(conversion.destination_items) == 3
    assert len(conversion.source_items) == 0


def test_one_to_one_matching():
    """
    As part of instansiation each source item should know how many source items and destination items have matching criteria
    """
    mock_source_1 = MockSource()
    mock_source_2 = MockSource()
    mock_source_3 = MockSource()
    mock_source_4 = MockSource()

    conversion = Conversion(
        source_items={
            mock_source_1: "A",
            mock_source_2: "A",
            mock_source_3: "B",
            mock_source_4: "C"

        },
        destination_items={
            MockDestination(): "A",
            MockDestination(): "B",
            MockDestination(): "B",
            MockDestination(): "D",

        },
        source_object=MockSource,
        destination_object=MockDestination
    )

    assert conversion.source_items_and_counters[mock_source_1] == ("A", [2, 1])
    assert conversion.source_items_and_counters[mock_source_2] == ("A", [2, 1])
    assert conversion.source_items_and_counters[mock_source_3] == ("B", [1, 2])
    assert conversion.source_items_and_counters[mock_source_4] == ("C", [1, 0])
