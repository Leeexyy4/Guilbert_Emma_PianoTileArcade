import pygame, librosa, random
from ui.utils.note import Note

class Piano:
    def __init__(self, gameview):
        self.__gameView = gameview
        self.__filepath = f"./assets/music/{self.__gameView.getWindowManager().getMusicSelect().lower().replace('play musique ', '').replace(' ', '').replace("'", '').replace(',', '')}.mp3"
        self.__difficulty = 1
        self.__notes = self.generate_notes()

    def getNotes(self):
        return self.__notes

    def increaseDifficulty(self):
        self.__difficulty += 1

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.__filepath)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def generate_notes(self):
        notes = []

        duration_per_chunk = 10  # secondes par bloc
        max_notes_per_beat = max(1, self.__difficulty // 2)  # Réduction du nombre de notes

        # Charge seulement les caractéristiques nécessaires (mono, sr adapté)
        y_full, sr = librosa.load(self.__filepath, sr=22050, mono=True)  # sr plus petit = moins de mémoire
        total_duration = librosa.get_duration(y=y_full, sr=sr)
        num_chunks = int(total_duration // duration_per_chunk) + 1

        for i in range(num_chunks):
            start_sample = int(i * duration_per_chunk * sr)
            end_sample = int(min((i + 1) * duration_per_chunk * sr, len(y_full)))
            y_chunk = y_full[start_sample:end_sample]

            # Analyse rythmique
            _, beat_frames = librosa.beat.beat_track(y=y_chunk, sr=sr)
            beat_times = librosa.frames_to_time(beat_frames, sr=sr)
            beat_times = beat_times[::2]  # ✅ Garde 1 beat sur 2

            for t in beat_times:
                timestamp = t + i * duration_per_chunk

                # ✅ Réduction du nombre de notes générées
                nb_notes = min(max_notes_per_beat, random.randint(1, 2))  # max 1-2 notes
                for _ in range(nb_notes):
                    position = random.choice(["left", "middle", "right", "top"])
                    note = Note(gameview=self.__gameView, position=position, timestamp=timestamp)
                    notes.append(note)

        return notes

    def getCurrentTime(self):
        return pygame.mixer.music.get_pos() / 1000.0
