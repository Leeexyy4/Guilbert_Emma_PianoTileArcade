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

    def setSelection(self, page, selection):
        """Met à jour la sélection pour la page donnée."""
        self.__selections[page] = selection

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
        
        # Si déplacement horizontal (gauche ou droite)
        if dy != 0 and dx == 0:
            nouvelle_col = y + dy
            candidats = [(i, j) for (i, j) in self.getPositions(page) if j == nouvelle_col]
            if candidats:
                # Trouver la ligne la plus proche de la position actuelle
                candidats.sort(key=lambda pos: abs(pos[0] - x))
                self.__position[page] = list(candidats[0])
                print(f"Position horizontale ajustée : {self.getPosition(page)}")
        
        # Si déplacement vertical (haut ou bas)
        elif dx != 0 and dy == 0:
            nouvelle_ligne = x + dx
            candidats = [(i, j) for (i, j) in self.getPositions(page) if i == nouvelle_ligne]
            if candidats:
                # Trouver la colonne la plus proche de la position actuelle
                candidats.sort(key=lambda pos: abs(pos[1] - y))
                self.__position[page] = list(candidats[0])
                print(f"Position verticale ajustée : {self.getPosition(page)}")
        
        self.getSelection(page).update_selection(page, direction, self.getPosition(page))
        print(f"Déplacement invalide depuis {self.getPosition(page)} vers {tentative}")
