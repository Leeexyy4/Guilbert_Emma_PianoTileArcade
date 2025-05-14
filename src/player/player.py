class Player:
    def __init__(self, name: str, score: int = 0):
        self._name = name
        self._score = score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Score must be a non-negative integer.")
        self._score = value