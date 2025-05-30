from enum import Enum

class PageState(Enum):
    PROFIL = 1
    TRIER = 2
    FILTRER = 3
    AIDE = 4
    DETAIL = 5
    PLAY = 6
    ACCUEIL = 7
    MULTIJOUEUR = 8
    STATISTIQUE = 9
    QUITTER = 10
    FIN_JEU_PERTE = 11
    FIN_JEU_GAIN = 12
