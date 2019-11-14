from zombie_invasion.human import Human


def test_human_colour_default():
    human = Human()
    assert human.colour == 'H'
