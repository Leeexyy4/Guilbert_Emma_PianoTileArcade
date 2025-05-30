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
            # Deuxième joueur
            pygame.K_KP1: False,
            pygame.K_KP2: False,
            pygame.K_KP3: False,
            pygame.K_KP4: False,
            pygame.K_KP5: False,
            pygame.K_KP6: False,  # Entrer
        }

    def update(self, event):
        """Met à jour l'état des boutons (1 à 6)."""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_z):
                return (0, -1)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                return (0, 1)
            elif event.key in (pygame.K_LEFT, pygame.K_q):
                return (-1, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                return (1, 0)
            if event.key in (pygame.K_KP6, pygame.K_6):
                return "enter"
        return None
