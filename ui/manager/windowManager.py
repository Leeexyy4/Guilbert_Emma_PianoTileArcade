import pygame
from core.music import Music
from ui.layout.gameView import GameView
from ui.utils.color import Color
from ui.layout.backgroundView import BackgroundView
# from ui.layout.gameView import GameView
from ui.layout.menuView import MenuView
from ui.layout.musicView import MusicView
from ui.layout.selectionView import SelectionView

class WindowManager:
    def __init__(self, interface):
        self.__interface = interface
        self.__window = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.DOUBLEBUF)
        self.__screenWidth = pygame.display.Info().current_w
        self.__screenHeight = pygame.display.Info().current_h
        self.__fontTall = pygame.font.Font('./assets/font/Tinos-Regular.ttf', 40)
        self.__fontSmall = pygame.font.Font('./assets/font/Tinos-Regular.ttf', 30)
        self.__color = Color()
        self.__scrollOffset: int = 0
        self.__musicSelect: Music = None
        self.__areaMusic: pygame.Rect = pygame.Rect(50, 200, self.__screenWidth - 100, self.__screenHeight - 375)
        self.__background: BackgroundView = BackgroundView(self)
        self.__music: MusicView = MusicView(self)
        self.__menu: MenuView = MenuView(self)
        self.__selection: SelectionView = SelectionView(self)
        
        if (self.__musicSelect != None):
            self.__game: GameView = GameView(self)

    def getInterface(self):
        return self.__interface
    
    def getWindow(self):
        return self.__window

    def getScreenWidth(self):
        return self.__screenWidth

    def getScreenHeight(self):
        return self.__screenHeight

    def getFontTall(self):
        return self.__fontTall

    def getFontSmall(self):
        return self.__fontSmall

    def getColor(self):
        return self.__color
    
    def getMusicSelect(self):
        return self.__musicSelect

    def getAreaMusic(self):
        """Retourne la sélection active pour une page."""
        return self.__areaMusic
    
    def getScrollOffset(self):
        """Retourne la sélection active pour une page."""
        return self.__scrollOffset
    
    def setScrollOffset(self, offset):
        """ Met à jour le décalage de défilement sans sortir de la zone visible. """
        self.__scrollOffset = self.__scrollOffset + offset
        # Limiter le décalage pour rester dans la zone visible
        if self.__scrollOffset < 0:
            self.__scrollOffset = 0
        elif self.__scrollOffset > self.__areaMusic.height:
            self.__scrollOffset = self.__areaMusic.height
    
    def setMusicSelect(self, musicSelect):
        """ Met à jour la selection de la musique. """
        self.__musicSelect = musicSelect
    
    def getBackground(self):
        """Affiche le fond d'écran."""
        return self.__background
    
    def getMusic(self):
        """Affiche la liste des musiques."""
        return self.__music
    
    def getMenu(self):
        """Affiche le menu."""
        return self.__menu
    
    def getSelection(self):
        """Affiche la selection."""
        return self.__selection
    
    def getGame(self):
        """Affiche le jeu."""
        return self.__game
    