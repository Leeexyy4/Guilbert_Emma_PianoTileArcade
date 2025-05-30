import pygame
from core.pageState import PageState  # Assure-toi d'importer les états de page

class MenuView:
    def __init__(self, windowManager):
        self.__windowManager = windowManager

    def affichageMenu(self):
        page = self.__windowManager.getInterface().getPage()

        # Cercle image de profil
        pygame.draw.circle(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), (100, 100), 80)
        pygame.draw.circle(self.__windowManager.getWindow(), self.__windowManager.getColor().getRose(), (100, 100), 75)
        pygame.draw.circle(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), (100, 100), 70)

        # Cercle icône aide
        pygame.draw.circle(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), (self.__windowManager.getScreenWidth() - 120, 100), 45)
        pygame.draw.circle(self.__windowManager.getWindow(), self.__windowManager.getColor().getRose(), (self.__windowManager.getScreenWidth() - 120, 100), 40)
        pygame.draw.circle(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), (self.__windowManager.getScreenWidth() - 120, 100), 35)

        # Boutons du haut (sauf pour la page "PROFIL")
        if page != PageState.PROFIL:
            rect = pygame.draw.rect(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), pygame.Rect((self.__windowManager.getScreenWidth() - 550) // 2, 80, 250, 50), border_radius=30)
            filter_trier = self.__windowManager.getFontSmall().render("Trier", True, self.__windowManager.getColor().getBlanc())
            self.__windowManager.getWindow().blit(filter_trier, filter_trier.get_rect(center=rect.center))

            rect = pygame.draw.rect(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), pygame.Rect((self.__windowManager.getScreenWidth() + 100) // 2, 80, 250, 50), border_radius=30)
            filter_filtres = self.__windowManager.getFontSmall().render("Filtrer", True, self.__windowManager.getColor().getBlanc())
            self.__windowManager.getWindow().blit(filter_filtres, filter_filtres.get_rect(center=rect.center))

        # Boutons du bas (global)
        rect_bouton = pygame.Rect(0, self.__windowManager.getScreenHeight() - 150, self.__windowManager.getScreenWidth(), 150)
        pygame.draw.rect(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), rect_bouton)

        
        texts = ["Accueil", "Multijoueur", "Statistique", "Quitter"]
        for i, text in enumerate(texts):
            x_center = self.__windowManager.getScreenWidth() * (i + 0.5) / 4
            text_surface = self.__windowManager.getFontTall().render(text, True, self.__windowManager.getColor().getBlanc())
            text_rect = text_surface.get_rect(center=(x_center, self.__windowManager.getScreenHeight() - 75))
            self.__windowManager.getWindow().blit(text_surface, text_rect)

        # Séparateurs verticaux
        for i in range(1, 4):
            x = self.__windowManager.getScreenWidth() * i / 4
            pygame.draw.line(
                self.__windowManager.getWindow(),
                self.__windowManager.getColor().getRose(),
                (x, self.__windowManager.getScreenHeight() - 150),
                (x, self.__windowManager.getScreenHeight()),
                5
            )

        self.affichageMenuSelonPage(self.__windowManager.getInterface().getPage())

    def affichageMenuSelonPage(self, page):
        # Liste de Musique Flou
        if page == PageState.TRIER or page == PageState.FILTRER:
            # Taille de la surface
            x, y = 50, 200
            w, h = self.__windowManager.getScreenWidth() - 100, self.__windowManager.getScreenHeight() - 375

            # Capturer le fond actuel à cet endroit
            fond_rect = pygame.Rect(x, y, w, h)
            fond_capture = self.__windowManager.getWindow().subsurface(fond_rect).copy()

            # Appliquer un flou en downscalant/upscalant
            small = pygame.transform.smoothscale(fond_capture, (w // 10, h // 10))
            blurry = pygame.transform.smoothscale(small, (w, h))

            # Créer une surface finale transparente
            surface_finale = pygame.Surface((w, h), pygame.SRCALPHA)
            surface_finale.blit(blurry, (0, 0))

            # Ajouter un voile semi-transparent violet
            voile = pygame.Surface((w, h), pygame.SRCALPHA)
            voile.fill((150, 100, 200, 100))  # (R, G, B, alpha)
            surface_finale.blit(voile, (0, 0))

            # Dessiner le tout sur la fenêtre
            self.__windowManager.getWindow().blit(surface_finale, (x, y))
            # Cas spécial : PROFIL
            if page == PageState.PROFIL:
                center_x = self.__windowManager.getScreenWidth() // 2
            
                # Se connecter
                rect_connexion = pygame.Rect(center_x - 200, self.__windowManager.getScreenHeight() // 2 - 80, 400, 60)
                pygame.draw.rect(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), rect_connexion, border_radius=20)
                texte_connexion = self.__windowManager.getFontTall().render("Se connecter", True, self.__windowManager.getColor().getBlanc())
                self.__windowManager.getWindow().blit(texte_connexion, texte_connexion.get_rect(center=rect_connexion.center))

                # S'inscrire
                rect_inscription = pygame.Rect(center_x - 200, self.__windowManager.getScreenHeight() // 2 + 20, 400, 60)
                pygame.draw.rect(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), rect_inscription, border_radius=20)
                texte_inscription = self.__windowManager.getFontTall().render("S'inscrire", True, self.__windowManager.getColor().getBlanc())
                self.__windowManager.getWindow().blit(texte_inscription, texte_inscription.get_rect(center=rect_inscription.center))

        # Cas spécial : différent de ACCUEIL
        if page != PageState.ACCUEIL:
            rect_retour = pygame.Rect(30, 220, 140, 40)  # En dessous du cercle
            pygame.draw.rect(self.__windowManager.getWindow(), self.__windowManager.getColor().getViolet(), rect_retour, border_radius=15)
            texte_retour = self.__windowManager.getFontSmall().render("Retour", True, self.__windowManager.getColor().getBlanc())
            self.__windowManager.getWindow().blit(texte_retour, texte_retour.get_rect(center=rect_retour.center))
