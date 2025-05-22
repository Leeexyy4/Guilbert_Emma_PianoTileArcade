import pygame
from src.game.game import PageState
from src.interface.color import Color

class Selection:
    def __init__(self, interface, positions_valides=None):
        """Initialise la sélection avec l'interface et les positions valides."""
        self.__interface = interface
        self.__positions_valides = positions_valides
        self.__selections = {
            PageState.DEMARRAGE: self.create_demarrage_selections(self.__positions_valides),
        }

    def getInterface(self):
        """Getter de l'interface."""
        return self.__interface
    
    def getSelection(self, page):
        """Retourne la sélection pour la page donnée."""
        return self.__selections.get(page, None)
    
    def create_demarrage_selections(self, positions_valides):
        """Crée les sélections du tableau de démarrage en associant les positions valides aux sélections."""
        # Initialisation des sélections avec les formes fixes
        selections = {
            (0, 0): ("cercle", 100, 100, 75, self.getInterface().getCouleur().getNoir()),  # Rectangle
            (1, 0): ("rectangle", (self.getInterface().getScreenWidth() - 550) // 2, 80, 250, 50, self.getInterface().getCouleur().getNoir()),  # Rectangle
            (2, 0): ("rectangle", (self.getInterface().getScreenWidth() + 100) // 2, 80, 250, 50, self.getInterface().getCouleur().getNoir()),  # Rectangle
            (3, 0): ("cercle", self.getInterface().getScreenWidth() - 120, 100, 40, self.getInterface().getCouleur().getNoir()),  # Rectangle
        }

        # Configuration des musiques et autres éléments...
        index = (0, 0)
        for music in self.getInterface().getListeMusics():
            index = (index[0], index[1] + 1)
            # Ajouter une sélection pour chaque musique à une position valide
            if index in positions_valides:
                selections.update({
                    index: ("rectangle", 300, 125 + 210 * index[1] - self.getInterface().getScrollOffset(), 200, 50, self.getInterface().getCouleur().getNoir()),
                })
            index = (index[0] + 1, index[1])
            if index in positions_valides:
                selections.update({
                    index: ("rectangle", self.getInterface().getScreenWidth() - 260, 60 + 210 * index[1] - self.getInterface().getScrollOffset(), 200, 120, self.getInterface().getCouleur().getNoir()),
                })
            index = (0, index[1])

        # Ajouter les sélections pour les positions en bas de l'écran
        selections.update({
            (0, index[1] + 1): ("rectangle", 0, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getNoir()),  # Rectangle
            (1, index[1] + 1): ("rectangle", self.getInterface().getScreenWidth() / 4, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getNoir()),  # Rectangle
            (2, index[1] + 1): ("rectangle", self.getInterface().getScreenWidth() / 2, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getNoir()),  # Rectangle
            (3, index[1] + 1): ("rectangle", self.getInterface().getScreenWidth() * 3 / 4, self.getInterface().getScreenHeight() - 100, self.getInterface().getScreenWidth() / 4, 100, self.getInterface().getCouleur().getNoir()),  # Rectangle
        })

        return selections

    def update_selection(self, page, direction, position):
        """Met à jour la sélection pour la page donnée à la position spécifiée."""
        selection_dict = self.getSelection(page).copy()

        selection = selection_dict.copy()
        for key in selection_dict:
            if key[1] == 0 or key[1] == len(self.getInterface().getListeMusics()) + 1:
                selection.pop(key)

        # Direction vers le haut
        scroll_up = False
        if direction == (0, -1):
            y_first = selection[next(iter(selection))][2] 
            y_attendu = 335 + 210 * (len(self.getInterface().getListeMusics()) - 2)
            for i in range (1, self.getInterface().getScrollOffset() // 210 + 1):
                y_attendu -= i * 210
            y_attendu -= 514
            if y_first == 335 or y_first == y_attendu:
                print(f"✔️ La coordonnée y est bien égale à 335 ou {y_attendu}")
                for pos, forme in selection.items():
                    if pos == tuple(position):
                        if forme[2] - forme[4] < self.getInterface().getAreaMusique().top:
                            scroll_up = True
                            print("❌ Le rectangle est en dehors de l'aire de musique")
            else:
                print(f"❌ La coordonnée y n'est pas égale à 335 ou {y_attendu}")
                for pos, forme in selection.items():
                    if pos == tuple(position):
                        if forme[2] - forme[4] < self.getInterface().getAreaMusique().top:
                            scroll_up = True
                            print("❌ Le rectangle est en dehors de l'aire de musique")

            if scroll_up:
                for pos, forme in selection.items():
                    if forme[0] == "rectangle":
                        y = forme[2]
                        if (self.getInterface().getScrollOffset() // 210 >= 0):
                            y += 210
                        else:
                            y += self.getInterface().getScrollOffset()
                        selection_dict[pos] = ("rectangle", forme[1], y, forme[3], forme[4], forme[5])
                if (self.getInterface().getScrollOffset() // 210 < 0):
                    self.getInterface().setScrollOffset(-self.getInterface().getScrollOffset())
                else:
                    self.getInterface().setScrollOffset(-210)

        # Direction vers le bas
        scroll_down = False
        if direction == (0, 1):
            y_first = selection[next(iter(selection))][2] 
            y_attendu = 335 + 210 * (len(self.getInterface().getListeMusics()) - 2)
            for i in range (1, self.getInterface().getScrollOffset() // 210 + 1):
                y_attendu += i * 210
            y_attendu += 514
            if y_first == 335 or y_first == y_attendu:
                print("✔️ La coordonnée y est bien égale à 335")
                for pos, forme in selection.items():
                    if pos == tuple(position):
                        if forme[2] + forme[4] > self.getInterface().getAreaMusique().top + self.getInterface().getAreaMusique().height:
                            scroll_down = True
                            print("❌ Le rectangle est en dehors de l'aire de musique")
            else:
                print("❌ La coordonnée y n'est pas égale à 335 ou {y_attendu}")
                for pos, forme in selection.items():
                    if pos == tuple(position):
                        if forme[2] + forme[4] > self.getInterface().getAreaMusique().top + self.getInterface().getAreaMusique().height:
                            scroll_down = True
                            print("❌ Le rectangle est en dehors de l'aire de musique")

            if scroll_down:
                for pos, forme in selection.items():
                    if forme[0] == "rectangle":
                        y = forme[2]
                        if (self.getInterface().getScrollOffset() // 210 >= 0):
                            y -= 210
                        else:
                            y -= self.getInterface().getScrollOffset()
                        selection_dict[pos] = ("rectangle", forme[1], y, forme[3], forme[4], forme[5])
                if (self.getInterface().getScrollOffset() // 210 < 0):
                    self.getInterface().setScrollOffset(self.getInterface().getScrollOffset())
                else:
                    self.getInterface().setScrollOffset(210)
        
        if scroll_down or scroll_up:
            self.getInterface().getTableauManager().setSelection(page, Selection(self.getInterface(), selection_dict))
            
            