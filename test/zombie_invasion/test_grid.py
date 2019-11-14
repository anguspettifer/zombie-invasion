from zombie_invasion.grid import Grid, Square


def test_square_renders_empty_by_default():
    square = Square()
    assert square.render == "|_|"
