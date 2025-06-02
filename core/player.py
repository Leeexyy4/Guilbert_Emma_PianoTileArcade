class Player:
    def __init__(self, player_id, name, password):
        self.id = player_id
        self.name = name
        self.password = password

    def __repr__(self):
        return f"<Player id={self.id}, name='{self.name}'>"
