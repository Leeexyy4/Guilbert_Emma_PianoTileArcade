class Piano:
    def __init__(self):
        self._keys = []

    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, keys):
        if not isinstance(keys, list):
            raise ValueError("Keys must be a list.")
        self._keys = keys