from src.interface.selection import Selection
from src.interface.tableau import Tableau
from src.game.game import PageState

class TableauManager:
    def __init__(self, interface):
        # Initialisation des sélections et des tableaux selon l'état des pages
        self.__interface = interface

        self._positions_valides = {
            PageState.DEMARRAGE: self.__create_demarrage_positions(),
        }

        self.__selections = {
            PageState.DEMARRAGE: Selection(interface, self._positions_valides[PageState.DEMARRAGE]),
        }
        
        self.__tableaux = {
            PageState.DEMARRAGE: Tableau(interface, self._positions_valides[PageState.DEMARRAGE]),
        }

        # Gestion de la position dans TableauManager
        self.__position = {
            PageState.DEMARRAGE: (0, 0)  # Position initiale de démarrage
        }

    def getInterface(self):
        """Getter de l'interface."""
        return self.__interface

    def __create_demarrage_positions(self):
        """Crée les positions valides pour le tableau de démarrage."""
        positions_valides = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
        ]
        index = (0, 0)
        for music in self.getInterface().getListeMusics():
            index = (index[0], index[1] + 1)
            positions_valides.append(index)  # Ajouter la position valide pour la musique
            index = (index[0] + 1, index[1])
            positions_valides.append(index)  # Ajouter la position valide pour l'élément suivant
            index = (0, index[1])

        # Ajouter les positions des boutons en bas
        positions_valides.extend([
            (0, index[1] + 1),
            (1, index[1] + 1),
            (2, index[1] + 1),
            (3, index[1] + 1),
        ])

        return positions_valides

    def getSelection(self, page):
        """Retourne la sélection pour la page donnée."""
        return self.__selections.get(page, None)

    def getTableau(self, page):
        """Retourne le tableau pour la page donnée."""
        return self.__tableaux.get(page, None)
    
    def getPositions(self, page):
        """Retourne les positions valides pour la page donnée."""
        return self._positions_valides.get(page, None)
    
    def getPosition(self, page):
        """Retourne la position actuelle pour la page donnée."""
        return self.__position.get(page, None)

    def updatePosition(self, page, direction):
        """Met à jour la position sur le tableau en fonction de la direction, en respectant les positions valides."""
        dx, dy = direction
        x, y = self.getPosition(page)
        tentative = (x + dx, y + dy)

        selection_copy = dict(self.getSelection(page).getSelection(page))

        positions_to_remove = [
            pos for pos in selection_copy
            if pos[1] == 0 or pos[1] == len(self.getInterface().getListeMusics()) + 1
        ]

        for pos in positions_to_remove:
            selection_copy.pop(pos)

        if tentative in self.getPositions(page):
            if (direction == (0, 1) or direction == (0, -1) and tentative in selection_copy):
                if (self.getSelection(page).getSelection(page)[tentative][2] > self.getInterface().getScreenHeight() - 200):
                    self.getInterface().setScrollOffset(200)
                    for pos, shape in selection_copy.items():
                        if len(shape) == 6:
                            forme, x, y, width, height, color = shape
                            new_y = y - 200
                            self.getSelection(page).getSelection(page)[pos] = (forme, x, new_y, width, height, color)
                if (self.getSelection(page).getSelection(page)[tentative][2] < 200):
                    self.getInterface().setScrollOffset(-200)
                    for pos, shape in selection_copy.items():
                        if len(shape) == 6:
                            forme, x, y, width, height, color = shape
                            new_y = y + 200
                            self.getSelection(page).getSelection(page)[pos] = (forme, x, new_y, width, height, color)

            self.__position[page] = list(tentative)
            print(f"Position mise à jour : {self.getPosition(page)}")
            return

        # Si déplacement horizontal (gauche ou droite)
        if dy != 0 and dx == 0:
            nouvelle_col = y + dy
            candidats = [(i, j) for (i, j) in self.getPositions(page) if j == nouvelle_col]
            if candidats:
                # Trouver la ligne la plus proche de la position actuelle
                candidats.sort(key=lambda pos: abs(pos[0] - x))
                self.__position[page] = list(candidats[0])
                print(f"Position horizontale ajustée : {self.getPosition(page)}")
                return

        print(f"Déplacement invalide depuis {self.getPosition(page)} vers {tentative}")