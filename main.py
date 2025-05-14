# GUILBERT Emma


# ----------------------- Jeu de plateau - Bibliotheques  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame
from src.game.game import PageState
from src.game.game import Game
from src.game.logic import Logic
from src.interface.interface import Interface

# ----------------------- Jeu de plateau - Logic du jeu ------------------------ #
class Main:
    def __init__(self):
        self.__game = Game() 
        self.__interface = Interface(self.getGame())
        self.__logic = Logic(self.getGame(), self.getInterface())

# ----------------------------------- Getter des élements ----------------------------------- #

    def getGame(self):
        """Getter des états du jeu'."""
        return self.__game

    def getInterface(self): 
        """Getter de l'interface."""
        return self.__interface
    
    def getLogic(self):
        """Getter de la logique."""
        return self.__logic

# ----------------------------------- Image.Page du jeu ----------------------------------- #

    def PageDemarrage(self):
        if (self.getGame().getUpdate()):
            self.getInterface().affichagePageDemarrage()
        self.getLogic().actionPageDemarrage()

    def PageStatistiques(self):
        if (self.getGame().getUpdate()):
            self.getInterface().affichagePageStatistiques()
        self.getLogic().actionPageStatistiques()

    def PageCommande(self):
        if (self.getGame().getUpdate()):
            self.getInterface().affichagePageCommande()
        self.getLogic().actionPageCommande()

    def PageFinGagne(self):
        if (self.getGame().getUpdate()):
            self.getInterface().affichagePageFinGagne()
        self.getLogic().actionPageFinGagne()

    def PageFinPerdu(self):
        if (self.getGame().getUpdate()):
            self.getInterface().affichagePageFinPerdu()
        self.getLogic().actionPageFinPerdu()

if __name__ == "__main__":
    # Initialisation du jeu
    pygame.init()
    
    # pygame.mixer.music.load("./assets/music/Musique_jeu.mp3")
    # pygame.mixer.music.play(-1,0.0,8)

    main = Main()

    # Boucle de jeu pour tous les joueurs encore en vie
    while main.getGame().getPage() not in [PageState.FINGAGNE, PageState.FINPERDU]:
        if main.getGame().getPage() is PageState.DEMARRAGE:
            main.PageDemarrage()

        elif main.getGame().getPage() is PageState.STATISTIQUE:
            main.PageStatistiques()

        elif main.getGame().getPage() is  PageState.COMMANDE:
            main.PageCommande()
        
        elif main.getGame().getPage() is  PageState.FINGAGNE:
            main.PageFinGagne()

        elif main.getGame().getPage() is  PageState.FINPERDU:
            main.PageFinPerdu() 

        # Mettre à jour l'affichage
        pygame.display.update()
