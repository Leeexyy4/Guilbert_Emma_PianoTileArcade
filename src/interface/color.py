class Color:
    """La classe Couleur est une classe qui permet de recuperer la couleur voulue grâce au getter."""
    
    def __init__(self) -> None:
        """Initialisation des couleurs."""
        self.__BLANC = (255, 255, 255)
        self.__VIOLET = (238, 169, 239)
        self.__ROSE = (245, 203, 246)
        self.__BLEU = (196, 253, 251)
        self.__NOIR = (0, 0, 0)

    def getBlanc(self):
        """Getter de la couleur Blanche."""
        return self.__BLANC

    def getBleu(self):
        """Getter de la couleur Bleu."""
        return self.__BLEU

    def getViolet(self):
        """Getter de la couleur Violet."""
        return self.__VIOLET

    def getRose(self):
        """Getter de la couleur Rose."""
        return self.__ROSE

    def getNoir(self):
        """Getter de la couleur Noir."""
        return self.__NOIR