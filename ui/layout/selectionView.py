import pygame
from core.pageState import PageState

class SelectionView:
    def __init__(self, windowManager):
        self.__windowManager = windowManager
        self.__selections = {
            PageState.PROFIL: (
                (0, 0),
                self.create_PROFIL_selections()
            ),
            PageState.TRIER: (
                (0, 0),
                self.create_TRIER_selections()
            ),
            PageState.ACCUEIL: (
                (0, 0),
                self.create_ACCUEIL_selections()
            )
        }
        
    def getWindowManager(self):
        return self.__windowManager.getWindow()
    
    def getSelection(self):
        return self.__selections.get(self.__windowManager.getInterface().getPage())
    
    def getSelectionFull(self):
        page = self.__windowManager.getInterface().getPage()
        return self.__selections[page]
    
    def getPosition(self):
        page = self.__windowManager.getInterface().getPage()
        if page in self.__selections:
            return tuple(self.__selections[page][0])  # Cast en tuple
        return None

    def setPosition(self, position):
        """Met à jour la position de sélection pour la page actuelle."""
        page = self.__windowManager.getInterface().getPage()
        if page in self.__selections:
            _, selection_dict = self.__selections[page]
            self.__selections[page] = (position, selection_dict)

    def setSelection(self, selection_dict):
        """Met à jour le dictionnaire de sélection pour la page actuelle."""
        page = self.__windowManager.getInterface().getPage()
        if page in self.__selections:
            position, _ = self.__selections[page]
            self.__selections[page] = (position, selection_dict)

    def setSelectionFull(self, position, selection_dict):
        page = self.__windowManager.getInterface().getPage()
        self.__selections[page] = (position, selection_dict)

    def affichageSelection(self, page: PageState):
        selection = self.getSelectionFull()
        if not selection:
            return
        position_courante, dict_selection = selection
        for position, (shape, *params) in dict_selection.items():
            if tuple(position) == tuple(position_courante):
                if params[0] == "rectangle":
                    _, x, y, width, height, color = params
                    pygame.draw.rect(self.__windowManager.getWindow(), color, pygame.Rect(x, y, width, height), border_radius=30, width=5)
                elif params[0] == "cercle":
                    _, x, y, radius, color = params
                    pygame.draw.circle(self.__windowManager.getWindow(), color, (x, y), radius, width=5)

    def create_PROFIL_selections(self):
        positions_valides = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (0, 1)
        ]
        
        selections = {}

        if ((0, 0), (1, 0), (2, 0), (3, 0) in positions_valides):
            selections[(0, 0)] = "Profil", "cercle", 100, 100, 75, self.__windowManager.getColor().getBlanc()
            selections[(1, 0)] = "Aide", "cercle", self.__windowManager.getScreenWidth() - 120, 100, 40, self.__windowManager.getColor().getBlanc()
            selections[(0, 1)] = "Retour", "rectangle", 30, 220, 140, 40, self.__windowManager.getColor().getBlanc()
            selections[(0, 2)] = "Se connecter", "rectangle", self.__windowManager.getScreenWidth() // 2 - 200, self.__windowManager.getScreenHeight() // 2 - 80, 400, 60, self.__windowManager.getColor().getBlanc()
            selections[(0, 3)] = "S'inscrire", "rectangle",  self.__windowManager.getScreenWidth() // 2 - 200, self.__windowManager.getScreenHeight() // 2 + 20, 400, 60, self.__windowManager.getColor().getBlanc()
            selections[(0, 4)] = "Accueil", "rectangle", 0, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()
            selections[(1, 4)] = "Multijoueur", "rectangle", self.__windowManager.getScreenWidth() / 4, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()
            selections[(2, 4)] = "Statistique", "rectangle", self.__windowManager.getScreenWidth() / 2, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()
            selections[(3, 4)] = "Quitter", "rectangle", self.__windowManager.getScreenWidth() * 3 / 4, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()

        return selections
    
    def create_TRIER_selections(self):
        positions_valides = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (0, 1)
        ]
        
        selections = {}

        if ((0, 0), (1, 0), (2, 0), (3, 0) in positions_valides):
            selections[(0, 0)] = "Profil", "cercle", 100, 100, 75, self.__windowManager.getColor().getBlanc()
            selections[(1, 0)] = "Aide", "cercle", self.__windowManager.getScreenWidth() - 120, 100, 40, self.__windowManager.getColor().getBlanc()
            selections[(0, 1)] = "Retour", "rectangle", 30, 220, 140, 40, self.__windowManager.getColor().getBlanc()
            selections[(0, 2)] = "Se connecter", "rectangle", self.__windowManager.getScreenWidth() // 2 - 200, self.__windowManager.getScreenHeight() // 2 - 80, 400, 60, self.__windowManager.getColor().getBlanc()
            selections[(0, 3)] = "S'inscrire", "rectangle",  self.__windowManager.getScreenWidth() // 2 - 200, self.__windowManager.getScreenHeight() // 2 + 20, 400, 60, self.__windowManager.getColor().getBlanc()
            selections[(0, 4)] = "Accueil", "rectangle", 0, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()
            selections[(1, 4)] = "Multijoueur", "rectangle", self.__windowManager.getScreenWidth() / 4, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()
            selections[(2, 4)] = "Statistique", "rectangle", self.__windowManager.getScreenWidth() / 2, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()
            selections[(3, 4)] = "Quitter", "rectangle", self.__windowManager.getScreenWidth() * 3 / 4, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()

        return selections
    
    def create_ACCUEIL_selections(self):
        """Crée les sélections du tableau de démarrage en associant les positions valides aux sélections."""
        positions_valides = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
        ]
        index = (0, 0)
        for music in self.__windowManager.getInterface().getGame().getDatabase().getMusic():
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

        selections = {}

        if ((0, 0), (1, 0), (2, 0), (3, 0) in positions_valides):
            selections[(0, 0)] = "Profil", "cercle", 100, 100, 75, self.__windowManager.getColor().getBlanc()
            selections[(1, 0)] = "Trier", "rectangle",  (self.__windowManager.getScreenWidth() - 550) // 2, 80, 250, 50, self.__windowManager.getColor().getBlanc()
            selections[(2, 0)] = "Filtrer", "rectangle",  (self.__windowManager.getScreenWidth() + 100) // 2, 80, 250, 50, self.__windowManager.getColor().getBlanc()
            selections[(3, 0)] = "Aide", "cercle", self.__windowManager.getScreenWidth() - 120, 100, 40, self.__windowManager.getColor().getBlanc()

        # Configuration des musiques et autres éléments...
        index = (0, 0)
        for music in self.__windowManager.getInterface().getGame().getDatabase().getMusic():
            index = (index[0], index[1] + 1)
            # Ajouter une sélection pour chaque musique à une position valide
            if index in positions_valides:
                selections.update({
                    index: (f"Détail musique {music[1]}", "rectangle", 300, 125 + 210 * index[1] - self.__windowManager.getScrollOffset(), 200, 50, self.__windowManager.getColor().getBlanc()),
                })
            index = (index[0] + 1, index[1])
            if index in positions_valides:
                selections.update({
                    index: (f"Play musique {music[1]}", "rectangle", self.__windowManager.getScreenWidth() - 260, 60 + 210 * index[1] - self.__windowManager.getScrollOffset(), 200, 120, self.__windowManager.getColor().getBlanc()),
                })
            index = (0, index[1])

        # Ajouter les sélections pour les positions en bas de l'écran
        selections.update({
            (0, index[1] + 1): ("Accueil", "rectangle", 0, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()),  # Rectangle
            (1, index[1] + 1): ("Multijoueur", "rectangle", self.__windowManager.getScreenWidth() / 4, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()),  # Rectangle
            (2, index[1] + 1): ("Statistique", "rectangle", self.__windowManager.getScreenWidth() / 2, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()),  # Rectangle
            (3, index[1] + 1): ("Quitter", "rectangle", self.__windowManager.getScreenWidth() * 3 / 4, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth() / 4, 150, self.__windowManager.getColor().getBlanc()),  # Rectangle
        })

        return selections
    
    def update_selection(self, direction):
        """Met à jour la sélection pour la page donnée à la position spécifiée."""
        selection_dict = self.getSelection()[1].copy()

        selection = selection_dict.copy()
        for key in selection_dict:
            if key[1] == 0 or key[1] == len (self.__windowManager.getInterface().getGame().getDatabase().getMusic()) + 1:
                selection.pop(key)

        # Direction vers le haut
        scroll_up = False
        if direction == (0, -1):
            y_first = selection[next(iter(selection))][3] 
            y_attendu = 335 + 210 * (len (self.__windowManager.getInterface().getGame().getDatabase().getMusic()) - 2)
            for i in range (1, self.__windowManager.getScrollOffset() // 210 + 1):
                y_attendu -= i * 210
            y_attendu -= 514
            if y_first == 335 or y_first == y_attendu:
                # print(f"✔️ La coordonnée y est bien égale à 335 ou {y_attendu}")
                for pos, forme in selection.items():
                    if pos == tuple(self.getSelection()[0]):
                        if forme[3] < self.__windowManager.getAreaMusic().top:
                            scroll_up = True
                            # print("❌ Le rectangle est en dehors de l'aire de musique")
            else:
                # print(f"❌ La coordonnée y n'est pas égale à 335 ou {y_attendu}")
                for pos, forme in selection.items():
                    if pos == tuple(self.getSelection()[0]):
                        if forme[3] < self.__windowManager.getAreaMusic().top:
                            scroll_up = True
                            # print("❌ Le rectangle est en dehors de l'aire de musique")

            if scroll_up:
                for pos, forme in selection.items():
                    if forme[1] == "rectangle":
                        y = forme[3]
                        if (self.__windowManager.getScrollOffset() // 210 >= 0):
                            y += 210
                        else:
                            y += self.__windowManager.getScrollOffset()
                        selection_dict[pos] = (forme[0], "rectangle", forme[2], y, forme[4], forme[5], forme[6])
                if (self.__windowManager.getScrollOffset() // 210 < 0):
                    self.__windowManager.setScrollOffset(-self.__windowManager.getScrollOffset())
                else:
                    self.__windowManager.setScrollOffset(-210)

        # Direction vers le bas
        scroll_down = False
        if direction == (0, 1):
            y_first = selection[next(iter(selection))][3] 
            y_attendu = 335 + 210 * (len (self.__windowManager.getInterface().getGame().getDatabase().getMusic()) - 2)
            for i in range (1, self.__windowManager.getScrollOffset() // 210 + 1):
                y_attendu += i * 210
            y_attendu += 514
            if y_first == 335 or y_first == y_attendu:
                # print("✔️ La coordonnée y est bien égale à 335")
                for pos, forme in selection.items():
                    if pos == tuple(self.getSelection()[0]):
                        if forme[3] + forme[5] > self.__windowManager.getAreaMusic().top + self.__windowManager.getAreaMusic().height:
                            scroll_down = True
                            # print("❌ Le rectangle est en dehors de l'aire de musique")
            else:
                # print("❌ La coordonnée y n'est pas égale à 335 ou {y_attendu}")
                for pos, forme in selection.items():
                    if pos == tuple(self.getSelection()[0]):
                        if forme[3] + forme[5] > self.__windowManager.getAreaMusic().top + self.__windowManager.getAreaMusic().height:
                            scroll_down = True
                            # print("❌ Le rectangle est en dehors de l'aire de musique")

            if scroll_down:
                for pos, forme in selection.items():
                    if forme[1] == "rectangle":
                        y = forme[3]
                        if (self.__windowManager.getScrollOffset() // 210 >= 0):
                            y -= 210
                        else:
                            y -= self.__windowManager.getScrollOffset()
                        selection_dict[pos] = (forme[0], "rectangle", forme[2], y, forme[4], forme[5], forme[6])
                if (self.__windowManager.getScrollOffset() // 210 < 0):
                    self.__windowManager.setScrollOffset(self.__windowManager.getScrollOffset())
                else:
                    self.__windowManager.setScrollOffset(210)
        
        if scroll_down or scroll_up:
            self.setSelection(selection_dict)
            
    def updatePosition(self, direction):
        """Met à jour la position sur le tableau en fonction de la direction, en respectant les positions valides."""
        dx, dy = direction
        x, y = self.getSelection()[0]
        # Si déplacement horizontal (haut ou bas)
        if dy != 0 and dx == 0:
            nouvelle_col = y + dy
            candidats = [(i, j) for (i, j) in self.getSelection()[1].keys() if j == nouvelle_col]
            if candidats:
                # Trouver la ligne la plus proche de la position actuelle
                candidats.sort(key=lambda pos: abs(pos[0] - x))
                self.setPosition(list(candidats[0]))
        
        # Si déplacement vertical (haut ou bas)
        elif dx != 0 and dy == 0:
            nouvelle_ligne = x + dx
            candidats = [(i, j) for (i, j) in self.getSelection()[1].keys() if i == nouvelle_ligne]
            if candidats:
                # Trouver la colonne la plus proche de la position actuelle
                candidats.sort(key=lambda pos: abs(pos[1] - y))
                self.setPosition(list(candidats[0]))
        
        if self.__windowManager.getInterface().getPage() == PageState.ACCUEIL:
            self.update_selection(direction)

