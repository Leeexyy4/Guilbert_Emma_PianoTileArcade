import pygame

class Button:
    def __init__(self):
        self.__buttons = {
            # Premier joueur
            pygame.K_1: False,
            pygame.K_2: False,
            pygame.K_3: False,
            pygame.K_4: False,
            pygame.K_5: False,
            pygame.K_6: False,  # Entrer
            # Deuxieme joueur
            pygame.K_KP1: False,
            pygame.K_KP2: False,
            pygame.K_KP3: False,
            pygame.K_KP4: False,
            pygame.K_KP5: False,
            pygame.K_KP6: False,  # Entrer
        }

    def update(self, event):
        """Met à jour l'état des boutons (1 à 6) et renvoie la direction ou la touche pressée."""
        if event.type != pygame.KEYDOWN:
            return None  # Ignore les événements non-clavier

        if event.key in (pygame.K_UP, pygame.K_z):
            return (0, -1)
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            return (0, 1)
        elif event.key in (pygame.K_LEFT, pygame.K_q):
            return (-1, 0)
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            return (1, 0)

        if event.key in (pygame.K_KP_6, pygame.K_6):
            return "enter"
        if event.key in (pygame.K_KP_1, pygame.K_1):
            return 0
        if event.key in (pygame.K_KP_2, pygame.K_2):
            return 1
        if event.key in (pygame.K_KP_3, pygame.K_3):
            return 2
        if event.key in (pygame.K_KP_4, pygame.K_4):
            return 3
        if event.key in (pygame.K_KP_5, pygame.K_5):
            return 4

        return None

    def getAll(self):
        """
        Retourne l'état de tous les boutons suivis sous forme de dictionnaire.
        Exemple : {pygame.K_1: False, pygame.K_2: True, ...}
        """
        return self.__buttons.copy()
