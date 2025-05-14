import pygame
from src.game.game import PageState
from src.interface.color import Color

class Selection:
    def __init__(self, interface, positions_valides=None):
        """Initialise la sélection avec l'interface et les positions valides."""
        self.__interface = interface
        self.__positions_valides = positions_valides
        self.__selections = {
            PageState.DEMARRAGE: self.__create_demarrage_selections(self.__positions_valides),
        }

    def getInterface(self):
        """Getter de l'interface."""
        return self.__interface
    
    def getSelection(self, page):
        """Retourne la sélection pour la page donnée."""
        return self.__selections.get(page, None)
    
    def __create_demarrage_selections(self, positions_valides):
        """Crée les sélections du tableau de démarrage en associant les positions valides aux sélections."""
        # Initialisation des sélections avec les formes fixes
        selections = {
            (0, 0): ("cercle", 100, 100, 75, self.getInterface().getCouleur().getViolet()),  # Rectangle
            (1, 0): ("rectangle", (self.getInterface().getScreenWidth() - 550) // 2, 80, 250, 50, self.getInterface().getCouleur().getViolet()),  # Rectangle
            (2, 0): ("rectangle", (self.getInterface().getScreenWidth() + 100) // 2, 80, 250, 50, self.getInterface().getCouleur().getViolet()),  # Rectangle
            (3, 0): ("cercle", self.getInterface().getScreenWidth() - 120, 100, 40, self.getInterface().getCouleur().getViolet()),  # Rectangle
        }

        # Configuration des musiques et autres éléments...
        index = (0, 0)
        for music in self.getInterface().getListeMusics():
            index = (index[0], index[1] + 1)
            # Ajouter une sélection pour chaque musique à une position valide
            if index in positions_valides:
                selections.update({
                    index: ("rectangle", 300, 125 + 210 * index[1], 200, 50, self.getInterface().getCouleur().getNoir()),
                })
            index = (index[0] + 1, index[1])
            if index in positions_valides:
                selections.update({
                    index: ("rectangle", self.getInterface().getScreenWidth() - 260, 60 + 210 * index[1], 200, 120, self.getInterface().getCouleur().getNoir()),
                })
            index = (0, index[1])

        # Ajouter les sélections pour les positions en bas de l'écran
        selections.update({
            (0, index[1] + 1): ("rectangle", 0, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getViolet()),  # Rectangle
            (1, index[1] + 1): ("rectangle", self.getInterface().getScreenWidth() / 4, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getViolet()),  # Rectangle
            (2, index[1] + 1): ("rectangle", self.getInterface().getScreenWidth() / 2, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getViolet()),  # Rectangle
            (3, index[1] + 1): ("rectangle", self.getInterface().getScreenWidth() * 3 / 4, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getViolet()),  # Rectangle
        })

        return selections
