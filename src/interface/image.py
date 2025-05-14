import pygame

class Image: 
    """La classe Image est une classe qui permet de recuperer l'image voulue grâce au getter."""
    class Page:
        """La classe Page est une classe qui permet de recuperer l'image voulue grâce au getter."""
        DEMARRAGE = pygame.image.load("./assets/img/page/demarrage.png")
        
    class Cover:
        """La classe Cover est une classe qui permet de recuperer la cover d'un album d'une musique."""
        SHAPEOFYOU = pygame.image.load("./assets/img/music/shapeofyou.png")
        BLINDINGLIGHTS = pygame.image.load("./assets/img/music/blindinglights.png")
        SOMEONEYOULOVED = pygame.image.load("./assets/img/music/someoneyouloved.png")
        SUNFLOWER = pygame.image.load("./assets/img/music/sunflower.png")
        SWEATERWEATHER = pygame.image.load("./assets/img/music/sweaterweather.png")
        BELIEVER = pygame.image.load("./assets/img/music/believer.png")