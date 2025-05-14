from enum import Enum
from src.database.database import Database

class PageState(Enum):
    DEMARRAGE = 1
    STATISTIQUE = 2
    COMMANDE = 3
    CHOIXPERSONNAGE = 4
    NBJOUEUR = 5
    FINGAGNE = 6
    FINPERDU = 7

class Game:
    def __init__(self):
        self.__page = PageState.DEMARRAGE
        self.__db = Database()
        self.__update = True

    def getPage(self):
        """Getter de la page."""
        return self.__page
    
    def getUpdate(self):
        """Getter de la mise à jour de l'affichage selon les clics."""
        return self.__update
    
    def getDb(self):
        """Getter de la base de données."""
        return self.__db
    
    # ----------------------------------- Setter des élements ----------------------------------- #

    def setPage(self, page):
        """Setter de la page."""
        self.__update = True
        self.__page = page

    def setUpdate(self, update):
        """Setter de la mise à jour de l'affichage selon les clics."""
        self.__update = update

    def setDb(self, db):
        """Setter de la base de données."""
        self.__db = db

