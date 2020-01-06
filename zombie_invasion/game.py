class Game:

    def __init__(self):
        self.dimensions = None
        self.number_of_humans = None

    def _request_dimensions(self):
        print("Please enter dimensions")
        self.dimensions = input()

    def _request_number_of_humans(self):
        print("Please enter number of humans")
        self.number_of_humans = input()

    def start(self):
        # self._request_dimensions()
        print("not tested")
