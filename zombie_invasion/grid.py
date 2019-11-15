class Square:
    def __init__(self, starter_square):
        self.__starter_square = starter_square

    @property
    def render(self):
        return self.__starter_square


class Row:
    def __init__(self, squares):
        self.__squares = squares

    @property
    def render(self):
        # Worries:
        # Knows that squares is a list
        # Knows that each sq has a method called render
        return "".join([sq.render for sq in self.__squares])


class Grid:
    def __init__(self, rows):
        self.__rows = rows

    @property
    def render(self):
        # Worries:
        # Knows that squares is a list
        # Knows that each sq has a method called render
        return "\n".join([sq.render for sq in self.__rows])
