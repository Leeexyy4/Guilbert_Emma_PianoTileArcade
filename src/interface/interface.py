# ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import random
import pygame
from src.game.game import Game, PageState
from src.interface.color import Color
from src.interface.image import Image
from src.interface.tableauManager import TableauManager
from src.interface.selection import Selection

class Interface:
    def __init__(self, game) -> None:
        """Initialisation de l'interface."""
        self.__fenetre = pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h), pygame.DOUBLEBUF)
        self.__scroll_offset = 0
        self.__game = game
        self.__listeMusics = self.__game.getDb().getMusic() 
        random.shuffle(self.__listeMusics)
        self.__screen_w = pygame.display.Info().current_w
        self.__screen_h = pygame.display.Info().current_h
        self.__policeG = pygame.font.Font('./assets/font/Tinos-Regular.ttf', 40)
        self.__policeP = pygame.font.Font('./assets/font/Tinos-Regular.ttf', 30)
        self.__couleur = Color()
        self.__tableau_selection_manager = TableauManager(self)
        
    
# ----------------------------------- Retournes élements ----------------------------------- #

    def getFenetre(self):
        """Retourne la fenêtre."""
        return self.__fenetre

    def getPoliceG(self):
        """Retourne la police."""
        return self.__policeG

    def getPoliceP(self):
        """Retourne la police."""
        return self.__policeP	
    
    def getGame(self):
        """Retourne la liste de joueur."""
        return self.__game
    
    def getListeMusics(self):
        """Retourne la liste de musique."""
        return self.__listeMusics
    
    def getTableauManager(self):
        """Retourne le tableau manager."""
        return self.__tableau_selection_manager
    
    def getTableau(self, page):
        """Retourne le tableau correspondant à la page actuelle."""
        tableau_selection = self.__tableau_selection_manager.getTableau(page)
        if tableau_selection:
            return tableau_selection
        return None

    def getSelection(self, page):
        """Retourne la sélection correspondant à la page actuelle."""
        tableau_selection = self.__tableau_selection_manager.getSelection(page)
        if tableau_selection:
            return tableau_selection
        return None

    def getScrollOffset(self):
        """Retourne le décalage de défilement."""
        return self.__scroll_offset
    
    def getScreenWidth(self):
        """Retourne la largeur de l'écran."""
        return self.__screen_w

    def getScreenHeight(self):
        """Retourne la hauteur de l'écran."""
        return self.__screen_h
    
    def getCouleur(self):
        """Retourne la couleur."""
        return self.__couleur
    
# ----------------------------------- Setter des élements ----------------------------------- #

    def setScrollOffset(self, offset):
        """ Met à jour le décalage de défilement sans sortir de la zone visible. """
        carte_hauteur = 210
        visible_zone = self.getScreenHeight() - 350
        total_hauteur = len(self.getListeMusics()) * carte_hauteur
        max_scroll = max(0, total_hauteur - visible_zone)
        self.__scroll_offset = max(0, min(self.__scroll_offset + offset, max_scroll))


# ----------------------------------- Affichage des élements ----------------------------------- #
    
    def affichageFondEcran(self, ImageFond):
        """
            La fonction affichageFondEcran permet d'afficher l'illustration de fond du jeu
            :param ImageFond: L'image de fond à afficher (par défaut, None).
        """
       
        self.getFenetre().blit(ImageFond, (0, 0))
        self.getFenetre().fill(self.getCouleur().getBlanc())

    def affichageMenu(self):
        """
            La fonction affichageMenu permet d'afficher le menu du jeu
        """
        # Cercle de l'image de profil
        pygame.draw.circle(self.getFenetre(), self.getCouleur().getRose(), (100, 100), 80)
        pygame.draw.circle(self.getFenetre(), self.getCouleur().getBleu(), (100, 100), 75)
        pygame.draw.circle(self.getFenetre(), self.getCouleur().getRose(), (100, 100), 70)
        
        # Cercle de l'icone d'aide
        pygame.draw.circle(self.getFenetre(), self.getCouleur().getRose(), (self.getScreenWidth() - 120, 100), 45)
        pygame.draw.circle(self.getFenetre(), self.getCouleur().getBleu(), (self.getScreenWidth() - 120, 100), 40)
        pygame.draw.circle(self.getFenetre(), self.getCouleur().getRose(), (self.getScreenWidth() - 120, 100), 35)

        # Rectangle des filtres et tries
        rect = pygame.draw.rect(self.getFenetre(), self.getCouleur().getRose(), pygame.Rect((self.getScreenWidth() - 550) // 2, 80, 250, 50), border_radius=30)
        filter_trier = self.getPoliceP().render("Trier", True, self.getCouleur().getNoir())
        self.getFenetre().blit(filter_trier, filter_trier.get_rect(center=rect.center))
        
        rect = pygame.draw.rect(self.getFenetre(), self.getCouleur().getRose(), pygame.Rect((self.getScreenWidth() + 100) // 2, 80, 250, 50), border_radius=30)
        filter_filtres = self.getPoliceP().render("Filtrer", True, self.getCouleur().getNoir())
        self.getFenetre().blit(filter_filtres, filter_filtres.get_rect(center=rect.center))

        rect_bouton = pygame.Rect(0, self.getScreenWidth() - 100, self.getScreenWidth(), 100)
        pygame.draw.rect(self.getFenetre(), self.getCouleur().getRose(), rect_bouton)

        # Textes des boutons
        texts = ["Accueil", "Multijoueur", "Statistiques", "Quitter"]
        for i, text in enumerate(texts):
            x_center = pygame.display.Info().current_w * (i + 0.5) / 4
            text_surface = self.getPoliceG().render(text, True, self.getCouleur().getNoir())
            text_rect = text_surface.get_rect(center=(x_center, self.getScreenHeight() - 50))
            self.getFenetre().blit(text_surface, text_rect)

        # Séparateurs verticaux
        pygame.draw.line(self.getFenetre(), self.getCouleur().getBleu(), (self.getScreenWidth() / 4, self.getScreenHeight() - 100), (self.getScreenWidth() / 4, self.getScreenHeight()), 5)
        pygame.draw.line(self.getFenetre(), self.getCouleur().getBleu(), (self.getScreenWidth() / 2, self.getScreenHeight() - 100), (self.getScreenWidth() / 2, self.getScreenHeight()), 5)
        pygame.draw.line(self.getFenetre(), self.getCouleur().getBleu(), (self.getScreenWidth() * 3 / 4, self.getScreenHeight() - 100), (self.getScreenWidth() * 3 / 4, self.getScreenHeight()), 5)

    def affichageListeMusique(self):
        """Affiche une liste défilante de musiques dans une zone scrollable."""

        scroll_area = pygame.Rect(50, 200, self.getScreenWidth() - 100, self.getScreenHeight() - 350)
        surface = pygame.Surface((scroll_area.width, scroll_area.height))
        surface.fill(self.getCouleur().getBleu())
                            
        for index, music in enumerate(self.getListeMusics()):
            top_y = index * 210 - self.getScrollOffset()
            if top_y + 200 < 0 or top_y > scroll_area.height:
                continue  # hors de la zone visible

            # Rectangle global
            rect = pygame.Rect(0, top_y, scroll_area.width, 200)
            pygame.draw.rect(surface, self.getCouleur().getRose(), rect, border_radius=30)

            # Couverture
            cover = music[1].upper().replace(" ", "").replace("'", "").replace(",", "").replace("é", "e")
            surface.blit(getattr(Image.Cover, cover), getattr(Image.Cover, cover).get_rect(left=rect.left, centery=rect.centery))

            # Titre
            title = self.getPoliceP().render(f"{music[1]} - {music[2]}", True, self.getCouleur().getNoir())
            surface.blit(title, title.get_rect(left=rect.left + 250, centery=rect.top + 60))

            # Bouton Détails
            rect_bouton = pygame.Rect(rect.left + 250, rect.top + 135, 200, 50)
            pygame.draw.rect(surface, self.getCouleur().getBleu(), rect_bouton, border_radius=30)
            detail_button_text = self.getPoliceP().render("Détails", True, self.getCouleur().getRose())
            surface.blit(detail_button_text, detail_button_text.get_rect(center=rect_bouton.center))

            # Difficulté
            pygame.draw.polygon(surface, self.getCouleur().getBleu(), [(rect.right - 210, rect.top), (rect.right - 250, rect.top), (rect.right - 210, rect.top + 49)])
            rect_diff = pygame.Rect(rect.right - 210, rect.top, 210, 50)
            pygame.draw.rect(surface, self.getCouleur().getBleu(), rect_diff)
            surface.blit(self.getPoliceP().render("Difficulté", True, self.getCouleur().getRose()), self.getPoliceP().render("Difficulté", True, self.getCouleur().getRose()).get_rect(center=rect_diff.center))

            # Bouton Play
            rect_play = pygame.Rect(rect.right - 210, rect.top + 70, 200, 115)
            pygame.draw.rect(surface, self.getCouleur().getBleu(), rect_play, border_radius=30)
            surface.blit(self.getPoliceP().render("Play", True, self.getCouleur().getRose()), self.getPoliceP().render("Play", True, self.getCouleur().getRose()).get_rect(center=rect_play.center))

        self.getFenetre().blit(surface, scroll_area.topleft, area=pygame.Rect(0, 0, scroll_area.width, scroll_area.height))


    def affichageSelection(self, page):
        """Affiche la sélection de la page actuelle."""
        selection = self.getSelection(page)
        if selection:
            for position, (shape, *params) in selection.getSelection(page).items():
                tableau_pos = self.getTableauManager().getPosition(page)
                if tuple(position) == tuple(tableau_pos):
                    if shape == "rectangle":
                        x, y, width, height, color = params
                        pygame.draw.rect(self.getFenetre(), color, pygame.Rect(x, y, width, height), border_radius=30, width=5)
                    elif shape == "cercle":
                        x, y, radius, color = params
                        pygame.draw.circle(self.getFenetre(), color, (x, y), radius, width=5)

# ----------------------------------- Affichage des élements des pages ----------------------------------- #

    def affichagePageDemarrage(self): 
        self.affichageFondEcran(Image.Page.DEMARRAGE) 
        self.affichageMenu()
        self.affichageListeMusique()
        self.affichageSelection(PageState.DEMARRAGE)

    def affichagePageStatistiques(self):
        self.affichageFondEcran(Image.Page.STATS)
        
    def affichagePageCommande(self):
        self.affichageFondEcran(Image.Page.COMMANDES)    

    def affichagePageFinPerdu(self):
        self.affichageFondEcran(Image.Page.FIN_JEU)
        self.affichageMenu()
                        
    def affichagePageFinGagne(self):
        self.affichageFondEcran(Image.Page.FIN_JEU)
        self.affichageMenu()