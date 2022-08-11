class Driver:
    DEFAULT_CAR = None
    DEFAULT_WINS = 0

    def __init__(self, name):
        self.name = name
        self.car = self.DEFAULT_CAR
        self.number_of_wins = self.DEFAULT_WINS

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.strip() == '':
            raise ValueError("Name should contain at least one character!")
        self.__name = value

