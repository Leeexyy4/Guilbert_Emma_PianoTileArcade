class Musique:
    def __init__(self, titre, auteur, niveau_de_difficulte, nombre_d_etoiles_remporte):
        self._titre = titre
        self._auteur = auteur
        self._niveau_de_difficulte = niveau_de_difficulte
        self._nombre_d_etoiles_remporte = nombre_d_etoiles_remporte

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, value):
        self._titre = value

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, value):
        self._auteur = value

    @property
    def niveau_de_difficulte(self):
        return self._niveau_de_difficulte

    @niveau_de_difficulte.setter
    def niveau_de_difficulte(self, value):
        self._niveau_de_difficulte = value

    @property
    def nombre_d_etoiles_remporte(self):
        return self._nombre_d_etoiles_remporte

    @nombre_d_etoiles_remporte.setter
    def nombre_d_etoiles_remporte(self, value):
        self._nombre_d_etoiles_remporte = value