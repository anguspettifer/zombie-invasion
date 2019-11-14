class Grid:
    def __init__(self):
        return False


class Square:
    def __init__(self):
        self.contains = None

    @property
    def render(self):
        if self.contains is None:
            return "|_|"
