import pygame

class SongSelection:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game  # Reference to the main game class
        self.font = pygame.font.SysFont(None, 36)
        # Define songs with their title, beatmap, and song file path
        self.songs = [
            {"title": "Song 1 - Artist A", "beatmap": "beatmap1_data", "song_file": "/data/Mixea_MediumNeutral_Beneath The Stars.mp3"},
            {"title": "Song 2 - Artist B", "beatmap": "beatmap2_data", "song_file": "path/to/song2.mp3"},
            {"title": "Song 3 - Artist C", "beatmap": "beatmap3_data", "song_file": "path/to/song3.mp3"},
        ]
        self.selected_index = 0

    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background for song selection
        title = self.font.render("Select a Song", True, (255, 255, 255))
        self.screen.blit(title, (20, 20))

        for i, song in enumerate(self.songs):
            color = (255, 255, 255) if i == self.selected_index else (100, 100, 100)
            song_text = self.font.render(song["title"], True, color)
            self.screen.blit(song_text, (20, 70 + i * 40))

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.songs)
            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.songs)
            elif event.key == pygame.K_RETURN:
                selected_song = self.songs[self.selected_index]
                self.game.load_song(selected_song["beatmap"], selected_song["song_file"])

    def play_song(self, song_file):
        # Load and play the selected song file
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()