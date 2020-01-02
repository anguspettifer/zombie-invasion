class Zombie:
    def __init__(self):
        self.render = 'Z'

    @staticmethod
    def _move_one_closer(x, y):
        if x > y:
            return x - 1
        elif x < y:
            return x + 1
        else:
            return x

    def move(self, zombie_coordinates, human_coordinates):
        for human, coordinates in human_coordinates.iteritems():
            closest_human = coordinates
        new_x_coordinates = self._move_one_closer(zombie_coordinates[0], closest_human[0])
        new_y_coordinates = self._move_one_closer(zombie_coordinates[1], closest_human[1])
        return [new_x_coordinates, new_y_coordinates]
