from src.game.game import PageState

class Tableau:
    def __init__(self, interface, positions_valides):
        """Initialise la sélection avec l'interface et les positions valides."""
        self.__interface = interface
        self.__positions_valides = positions_valides
        self.__positions = {
            PageState.DEMARRAGE: self.__create_demarrage_positions(self.__positions_valides),
        }

    def getInterface(self):
        """Getter de l'interface."""
        return self.__interface
    
    def getPositions(self, page):
        """Retourne les positions pour la page donnée."""
        return self.__positions.get(page, None)

    def __create_demarrage_positions(self, positions_valides):
        """Crée les positions du tableau de démarrage en associant les positions valides aux actions et musiques."""
        positions = {}

        # 4 premières positions pour actions fixes
        if (0, 0) in positions_valides:
            positions[(0, 0)] = "Profil"
        if (1, 0) in positions_valides:
            positions[(1, 0)] = "Trier"
        if (2, 0) in positions_valides:
            positions[(2, 0)] = "Filtrer"
        if (3, 0) in positions_valides:
            positions[(3, 0)] = "Aide"

        # Positions intermédiaires pour détails et jouer musiques (index dynamique)
        index = (0, 0)
        for music in self.getInterface().getListeMusics():
            index = (index[0], index[1] + 1)
            # Ajouter une sélection pour chaque musique à une position valide
            if index in positions_valides:
                positions.update({
                    index: (f"Détail musique {music}"),
                })
            index = (index[0] + 1, index[1])
            if index in positions_valides:
                positions.update({
                    index: (f"Play musique {music}"),
                })
            index = (0, index[1])

        # 4 dernières positions pour actions fixes
        positions.update({
            (0, index[1] + 1): "Accueil",
            (1, index[1] + 1): "Multijoueur",
            (2, index[1] + 1): "Statistiques",
            (3, index[1] + 1): "Quitter",
        })


        return positions
