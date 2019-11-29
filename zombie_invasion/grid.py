class BlankSquare:
    """Knows that is has a renderable state"""
    def __init__(self, starter_square):
        self.__starter_square = starter_square

    @property
    def render(self):
        return self.__starter_square


class Row:
    """Knows how to order squares to render a playing row
    Knows how to determin the location of a human in a row"""
    def __init__(self, squares):
        self.squares = squares
        self.human_location = []

    @property
    def human_in_row(self):
        human_location_list = []
        for i in range(len(self.squares)):
            if self.squares[i].render == 'H':
                human_location_list.append(i)
        return human_location_list

    def move_left(self):
        popped_square = self.squares.pop(0)
        self.squares.append(popped_square)

    @property
    def render(self):
        # Worries:
        # Knows that squares is a list
        # Knows that each sq has a method called render
        # Do I want to handle an exception here?
        # Could be an attribute error or a type error
        return "".join([sq.render for sq in self.squares])


class Grid:
    """Knows how to stack rows to render a playing grid"""
    def __init__(self, rows):
        self.rows = rows

    @property
    def render(self):
        return "\n".join([row.render for row in self.rows])

    def everybody_move(self):
        for row in self.rows:
            if row.human_in_row:
                row.move_left()
