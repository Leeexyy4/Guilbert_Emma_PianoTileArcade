class Projet:
    def __init__(self, titre, description, createur):
        self._titre = titre
        self._description = description
        self._createur = createur

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, value):
        self._titre = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def createur(self):
        return self._createur

    @createur.setter
    def createur(self, value):
        self._createur = value
