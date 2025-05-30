class Color:
    """La classe Color est une classe qui permet de recuperer la color voulue grâce au getter."""
    
    def __init__(self) -> None:
        """Initialisation des colors."""
        self.__BLANC = (255, 255, 255)
        self.__VIOLET = (238, 169, 239)
        self.__ROSE = (245, 203, 246)
        self.__BLEU = (196, 253, 251)
        self.__NOIR = (0, 0, 0)

    def getBlanc(self):
        """Getter de la color Blanche."""
        return self.__BLANC

    def getBleu(self):
        """Getter de la color Bleu."""
        return self.__BLEU

    def getViolet(self):
        """Getter de la color Violet."""
        return self.__VIOLET

    def getRose(self):
        """Getter de la color Rose."""
        return self.__ROSE

    def getNoir(self):
        """Getter de la color Noir."""
        return self.__NOIR