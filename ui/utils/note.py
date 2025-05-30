import pygame

class Note:
    def __init__(self, gameView):
        self.__column
        self.__width = gameView.getWindowManager().getScreenWidth() / 4
        self.__height = gameView.getWindowManager().getScreenHeight() / 6
        self.__rect
        self.clicked = False

    def move(self):
        self.__rect.y += 5

    def draw(self, screen):
        color = self if not self.clicked else (100, 100, 100)
        pygame.draw.rect(screen, color, self.__rect, border_radius=8)