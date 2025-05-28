import sqlite3
import os

class Database:
    def __init__(self, db_path="ressources/database/database.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)  # Permet les accès depuis plusieurs threads
        self.conn.execute('PRAGMA journal_mode=WAL;')  # Active le mode WAL
        self.cursor = self.conn.cursor()
        self.initialize()
        

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                FOREIGN KEY (player_name) REFERENCES players(name),
                FOREIGN KEY (score) REFERENCES music(title),
                UNIQUE(player_name, score)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT,
                UNIQUE(name, email)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS music (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                genre TEXT,
                release_date DATE,
                UNIQUE(title, artist)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                FOREIGN KEY (id) REFERENCES music(id),
                UNIQUE(name, description)
            );
        """)

        self.conn.commit()

    def insert_tables(self):
        self.cursor.execute("""
            INSERT OR IGNORE INTO music (title, artist, genre, release_date) VALUES
            ("Shape of You", "Ed Sheeran", "Pop", "2017-01-06"),
            ("Sunflower", "Post Malone & Swae Lee", "Hip Hop", "2018-10-18"),
            ("Sweater Weather", "The Neighbourhood", "Alternative Rock", "2013-03-28"),
            ("Believer", "Imagine Dragons", "Rock", "2017-02-01")
        """)

        self.cursor.execute("""
            INSERT OR IGNORE INTO scores (player_name, score) VALUES
            ('admin', 100)
        """)

        self.cursor.execute("""
            INSERT OR IGNORE INTO players (name, age, email) VALUES
            ('admin', 21, '123')
        """)

        self.cursor.execute("""
            INSERT OR IGNORE INTO playlists (name, description) VALUES
            ('My Playlist', 'A collection of my favorite songs')
        """)

        self.conn.commit()

    def initialize(self):
        """Initialise la base de données."""
        self.create_tables()
        self.insert_tables()
        print("Base de données initialisée.")

    # ----------------------------------- Getter des élements ----------------------------------- #

    def getMusic(self):
        """Getter de la musique."""
        self.cursor.execute("SELECT * FROM music")
        return self.cursor.fetchall()

    def getScores(self):
        """Getter des scores."""
        self.cursor.execute("SELECT * FROM scores")
        return self.cursor.fetchall()

    def getPlayers(self):
        """Getter des joueurs."""
        self.cursor.execute("SELECT * FROM players")
        return self.cursor.fetchall()

    def getPlaylists(self):
        """Getter des playlists."""
        self.cursor.execute("SELECT * FROM playlists")
        return self.cursor.fetchall()

    # ----------------------------------- Setter des élements ----------------------------------- #

    def setMusic(self, title, artist, genre, release_date):
        """Setter de la musique."""
        self.cursor.execute("INSERT INTO music (title, artist, genre, release_date) VALUES (?, ?, ?, ?)", (title, artist, genre, release_date))
        self.conn.commit()

    def setScores(self, player_name, score):
        """Setter des scores."""
        self.cursor.execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (player_name, score))
        self.conn.commit()

    def setPlayers(self, name, age, email):
        """Setter des joueurs."""
        self.cursor.execute("INSERT INTO players (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        self.conn.commit()

    def setPlaylists(self, name, description):
        """Setter des playlists."""
        self.cursor.execute("INSERT INTO playlists (name, description) VALUES (?, ?)", (name, description))
        self.conn.commit()

    # ----------------------------------- Add des élements ----------------------------------- #

    def addMusic(self, title, artist, genre, release_date):
        """Ajoute une musique à la base de données."""
        self.setMusic(title, artist, genre, release_date)
        print(f"Musique '{title}' ajoutée à la base de données.")

    def addScores(self, player_name, score):
        """Ajoute un score à la base de données."""
        self.setScores(player_name, score)
        print(f"Score de '{player_name}' ajouté à la base de données.")

    def addPlayers(self, name, age, email):
        """Ajoute un joueur à la base de données."""
        self.setPlayers(name, age, email)
        print(f"Joueur '{name}' ajouté à la base de données.")

    def addPlaylists(self, name, description):
        """Ajoute une playlist à la base de données."""
        self.setPlaylists(name, description)
        print(f"Playlist '{name}' ajoutée à la base de données.")

    # ----------------------------------- Edit des élements ----------------------------------- #

    def editMusic(self, music_id, title=None, artist=None, genre=None, release_date=None):
        """Modifie une musique dans la base de données."""
        if title:
            self.cursor.execute("UPDATE music SET title = ? WHERE id = ?", (title, music_id))
        if artist:
            self.cursor.execute("UPDATE music SET artist = ? WHERE id = ?", (artist, music_id))
        if genre:
            self.cursor.execute("UPDATE music SET genre = ? WHERE id = ?", (genre, music_id))
        if release_date:
            self.cursor.execute("UPDATE music SET release_date = ? WHERE id = ?", (release_date, music_id))
        self.conn.commit()
        print(f"Musique avec ID {music_id} modifiée.")

    def editScores(self, score_id, player_name=None, score=None):
        """Modifie un score dans la base de données."""
        if player_name:
            self.cursor.execute("UPDATE scores SET player_name = ? WHERE id = ?", (player_name, score_id))
        if score:
            self.cursor.execute("UPDATE scores SET score = ? WHERE id = ?", (score, score_id))
        self.conn.commit()
        print(f"Score avec ID {score_id} modifié.")

    def editPlayers(self, player_id, name=None, age=None, email=None):
        """Modifie un joueur dans la base de données."""
        if name:
            self.cursor.execute("UPDATE players SET name = ? WHERE id = ?", (name, player_id))
        if age:
            self.cursor.execute("UPDATE players SET age = ? WHERE id = ?", (age, player_id))
        if email:
            self.cursor.execute("UPDATE players SET email = ? WHERE id = ?", (email, player_id))
        self.conn.commit()
        print(f"Joueur avec ID {player_id} modifié.")

    def editPlaylists(self, playlist_id, name=None, description=None):
        """Modifie une playlist dans la base de données."""
        if name:
            self.cursor.execute("UPDATE playlists SET name = ? WHERE id = ?", (name, playlist_id))
        if description:
            self.cursor.execute("UPDATE playlists SET description = ? WHERE id = ?", (description, playlist_id))
        self.conn.commit()
        print(f"Playlist avec ID {playlist_id} modifiée.")

    # ----------------------------------- Delete des élements ----------------------------------- #

    def deleteMusic(self, music_id):
        """Supprime une musique de la base de données."""
        self.cursor.execute("DELETE FROM music WHERE id = ?", (music_id,))
        self.conn.commit()
        print(f"Musique avec ID {music_id} supprimée.")

    def deleteScores(self, score_id):
        """Supprime un score de la base de données."""
        self.cursor.execute("DELETE FROM scores WHERE id = ?", (score_id,))
        self.conn.commit()
        print(f"Score avec ID {score_id} supprimé.")

    def deletePlayers(self, player_id):
        """Supprime un joueur de la base de données."""
        self.cursor.execute("DELETE FROM players WHERE id = ?", (player_id,))
        self.conn.commit()
        print(f"Joueur avec ID {player_id} supprimé.")

    def deletePlaylists(self, playlist_id):
        """Supprime une playlist de la base de données."""
        self.cursor.execute("DELETE FROM playlists WHERE id = ?", (playlist_id,))
        self.conn.commit()
        print(f"Playlist avec ID {playlist_id} supprimée.")

    