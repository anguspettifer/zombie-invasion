from zombie_invasion.zombie import Zombie


def test_zombie_colour_default():
    zombie = Zombie()
    assert zombie.colour == 'Z'
