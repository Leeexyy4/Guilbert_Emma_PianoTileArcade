# ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import random, pygame
from core.pageState import PageState
from ui.manager.windowManager import WindowManager
from ui.utils.image import Image

class Interface:
    def __init__(self, game) -> None:
        """Initialisation de l'interface."""
        self.__game = game
        self.__update: bool = True
        self.__page: PageState = PageState.ACCUEIL
        self.__pagePrecedente: PageState = PageState.ACCUEIL
        self.__windowManager: WindowManager = WindowManager(self)
    
# ----------------------------------- Retournes élements ----------------------------------- #
    
    def getGame(self):
        """Game du jeu."""
        return self.__game
    
    def getWindowManager(self):
        """Retourne la fenêtre."""
        return self.__windowManager
    
    def getPage(self):
        """Retourne la page de l'interface."""
        return self.__page
    
    def getPagePrecedente(self):
        """Retourne la page precedente de l'interface."""
        return self.__pagePrecedente
    
    def getUpdate(self):
        """Retourne le booléen concernant la mise à jour de l'interface."""
        return self.__update
    
# ----------------------------------- Setter des élements ----------------------------------- #

    def setPage(self, page):
        """ Met à jour la page'. """
        self.setPagePrécédente(self.__page)
        self.__page = page

    def setPagePrécédente(self, pagePrecedente):
        """ Met à jour la page précédente'. """
        self.__pagePrecedente = pagePrecedente

    def setUpdate(self, update):
        """ Met à jour l'interface'. """
        self.__update = update

# ----------------------------------- Affichage des élements des pages ----------------------------------- #

    def affichagePageProfil(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.PROFIL)
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.PROFIL)

    def affichagePageTrier(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.TRIER)
        self.getWindowManager().getMusic().affichageListeMusique()
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.TRIER)

    def affichagePageFiltrer(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.FILTRER)
        self.getWindowManager().getMusic().affichageListeMusique()
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.FILTRER)

    def affichagePageAide(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.AIDE)   
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.AIDE) 

    def affichagePageDetail(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.DETAIL)
        self.getWindowManager().getMusic().affichageListeMusique()
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.DETAIL)
        
    def affichagePagePlay(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.PLAY)
        self.getWindowManager().getMusic().affichageListeMusique()
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.PLAY)
        
    def affichagePageAccueil(self): 
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.ACCUEIL) 
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getMusic().affichageListeMusique()
        self.getWindowManager().getSelection().affichageSelection(PageState.ACCUEIL)

    def affichagePageMultijoueur(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.MULTIJOUEUR)   
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.MULTIJOUEUR) 

    def affichagePageStatistique(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.STATISTIQUE)
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.STATISTIQUE)
        
    def affichagePageQuitter(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.QUITTER)
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.QUITTER)
        
    def affichagePageFinPerdu(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.FIN_JEU_PERTE)
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.FIN_JEU_PERTE)
                        
    def affichagePageFinGagne(self):
        self.getWindowManager().getBackground().affichageFondEcran(Image.Page.FIN_JEU_GAIN)
        self.getWindowManager().getMenu().affichageMenu()
        self.getWindowManager().getSelection().affichageSelection(PageState.FIN_JEU_GAIN)
