class Note:
    def __init__(self, name: str, frequency: float):
        self._name = name
        self._frequency = frequency

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Frequency must be a positive number.")
        self._frequency = value

    def __str__(self):
        return f"Note: {self.name}, Frequency: {self.frequency} Hz"

    def play(self):
        print(f"Playing {self.name} at {self.frequency} Hz")