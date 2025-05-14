#  ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import pygame
from src.interface.color import Color
from src.game.game import PageState, Game
from src.button.button import Button

# ----------------------- Jeu de plateau - Logic ------------------------ #
class Logic:
    def __init__(self, game, interface) -> None:
        """Initialisation de l'interface."""
        self.__mouse = pygame.mouse
        self.__game: Game = game
        self.__interface = interface
        self.__couleur: Color = Color()
        self.__button: Button = Button()

    def getMouse(self):
        """Getter de la souris."""
        return self.__mouse

    def getGame(self):
        """Getter de l'état du jeu."""
        return self.__game
    
    def getCouleur(self):
        """Getter de la couleur."""
        return self.__couleur
    
    def getInterface(self):
        """Getter de l'interface."""
        return self.__interface
    
    def getButton(self):
        """Getter du bouton."""
        return self.__button
    
# ----------------------------------- Affichage des élements ----------------------------------- #

    def actionPageDemarrage(self):
        self.getGame().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                self.getInterface().getTableauManager().updatePosition(PageState.DEMARRAGE, direction)
                self.getGame().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()


    def actionPageStatistiques(self):
        self.getGame().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:                
                self.getInterface().getTableauManager().updatePosition(PageState.STATISTIQUE, direction)
                self.getGame().setUpdate(True)

            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageCommande(self):
        self.getGame().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                tableau = self.getInterface().getTableau(PageState.DEMARRAGE)
                if tableau:
                    self.getInterface().getTableauManager().updatePosition(PageState.COMMANDE, direction)
                    self.getGame().setUpdate(True)

            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageFinGagne(self):
        self.getGame().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                tableau = self.getInterface().getTableau(PageState.DEMARRAGE)
                if tableau:
                    self.getInterface().getTableauManager().updatePosition(PageState.GAGNE, direction)
                    self.getGame().setUpdate(True)

            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageFinPerdu(self):
        self.getGame().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                tableau = self.getInterface().getTableau(PageState.DEMARRAGE)
                if tableau:
                    self.getInterface().getTableauManager().updatePosition(PageState.PERDU, direction)
                    self.getGame().setUpdate(True)

            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()