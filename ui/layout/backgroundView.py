import pygame

class BackgroundView:
    def __init__(self, windowManager):
        self.__windowManager = windowManager
        
    def affichageFondEcran(self, ImageFond):
        """
            La fonction affichageFondEcran permet d'affichage l'illustration de fond du jeu
            :param ImageFond: L'image de fond à affichage (par défaut, None).
        """
       
        # Récupère la taille de la fenêtre
        screen_width = self.__windowManager.getScreenWidth()
        screen_height = self.__windowManager.getScreenHeight()

        # Redimensionne l'image de fond à la taille de la fenêtre
        fond_redimensionne = pygame.transform.scale(ImageFond, (screen_width, screen_height))

        # Affiche l'image sur toute la fenêtre
        self.__windowManager.getWindow().blit(fond_redimensionne, (0, 0))
