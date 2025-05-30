#  ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import pygame
from ui.utils.color import Color
from core.pageState import PageState
from core.button import Button

# ----------------------- Jeu de plateau - Logic ------------------------ #
class Logic:
    def __init__(self, game) -> None:
        """Initialisation de l'interface."""
        self.__game = game
        self.__mouse = pygame.mouse
        self.__interface = game.getInterface()
        self.__color: Color = Color()
        self.__button: Button = Button()

    def getMain(self):
        """Game du jeu."""
        return self.__game
    
    def getMouse(self):
        """Getter de la souris."""
        return self.__mouse
    
    def getColor(self):
        """Getter de la color."""
        return self.__color
    
    def getInterface(self):
        """Getter de l'interface."""
        return self.__interface
    
    def getButton(self):
        """Getter du bouton."""
        return self.__button
    
# ----------------------------------- Affichage des élements ----------------------------------- #

    def actionPageProfil(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:    
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)              
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageTrier(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:            
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:              
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)                
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageFiltrer(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:              
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)              
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageAide(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()
                
    def actionPageDetail(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPagePlay(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageAccueil(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Profil"):
                        self.getInterface().setPage(PageState.PROFIL)
                        self.getInterface().setUpdate(True)
                    elif (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Trier"):
                        self.getInterface().setPage(PageState.TRIER)
                        self.getInterface().setUpdate(True)
                    elif (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Filtrer"):
                        self.getInterface().setPage(PageState.FILTRER)
                        self.getInterface().setUpdate(True)
                    elif (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Aide"):
                        self.getInterface().setPage(PageState.AIDE)
                        self.getInterface().setUpdate(True)
                    elif "Détail " in self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0]:
                        self.getInterface().getWindowManager().setMusicSelect(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0].replace("Détail musique ", ""))
                        self.getInterface().setPage(PageState.DETAIL)
                        self.getInterface().setUpdate(True)
                    elif "Play " in self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0]:
                        self.getInterface().getWindowManager().setMusicSelect(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0].replace("Play musique ", ""))
                        self.getInterface().setPage(PageState.PLAY)
                        self.getInterface().setUpdate(True)
                    elif (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Accueil"):
                        self.getInterface().setPage(PageState.ACCUEIL)
                        self.getInterface().setUpdate(True)
                    elif (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Multijoueur"):
                        self.getInterface().setPage(PageState.MULTIJOUEUR)
                        self.getInterface().setUpdate(True)
                    elif (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Statistique"):
                        self.getInterface().setPage(PageState.STATISTIQUE)
                        self.getInterface().setUpdate(True)
                    elif (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Quitter"):
                        self.getInterface().setPage(PageState.QUITTER)
                        self.getInterface().setUpdate(True)
                else:
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()
    
    def actionPageMultijoueur(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:    
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)            
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()
    
    def actionPageStatistique(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:             
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)               
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageQuitter(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:  
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)              
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageFinGagne(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()

    def actionPageFinPerdu(self):
        self.getInterface().setUpdate(False)
        for event in pygame.event.get():
            direction = self.getButton().update(event)
            if direction:
                if direction == "enter":
                    print(self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0])
                    if (self.getInterface().getWindowManager().getSelection().getSelection()[1][self.getInterface().getWindowManager().getSelection().getPosition()][0] == "Retour"):
                        self.getInterface().setPage(self.getInterface().getPagePrecedente())
                        self.getInterface().setUpdate(True)
                else:            
                    self.getInterface().getWindowManager().getSelection().updatePosition(direction)
                    self.getInterface().setUpdate(True)
            if event.type == pygame.QUIT:  # Quitter
                pygame.quit()
                exit()