from zombie_invasion.conversion import Conversion


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