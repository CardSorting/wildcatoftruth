import pygame
from song_selection import SongSelection
from beatmap import Beatmap  # Import your Beatmap class here

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = "splash"
        self.song_selection = SongSelection(screen, self)  # Ensure SongSelection is initialized correctly
        self.font = pygame.font.SysFont(None, 72)
        self.small_font = pygame.font.SysFont(None, 36)
        self.current_beatmap = None
        self.initialize_home_screen()

    def initialize_home_screen(self):
        self.buttons = [
            ("Play", self.screen.get_height() // 2 - 30),
            ("Options", self.screen.get_height() // 2 + 20),
            ("Exit", self.screen.get_height() // 2 + 70)
        ]

    def show_splash_screen(self):
        self.screen.fill((0, 0, 0))
        splash_text = self.font.render("Osu!mania Clone", True, (255, 255, 255))
        self.screen.blit(splash_text, (self.screen.get_width() // 2 - splash_text.get_width() // 2, self.screen.get_height() // 2 - splash_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.state = "home"

    def show_home_screen(self):
        self.screen.fill((255, 192, 203))  # Light pink background
        for button, position in self.buttons:
            button_text = self.small_font.render(button, True, (0, 0, 0))
            rect = button_text.get_rect(center=(self.screen.get_width() // 2, position))
            pygame.draw.rect(self.screen, (255, 255, 255), rect.inflate(20, 10), 1)  # Draw border
            self.screen.blit(button_text, button_text.get_rect(center=(self.screen.get_width() // 2, position)))
        pygame.display.flip()

    def load_song(self, beatmap_data, song_file):
        self.current_beatmap = Beatmap(beatmap_data)
        self.song_selection.play_song(song_file)
        self.state = "gameplay"

    def update(self):
        if self.state == "splash":
            self.show_splash_screen()
        elif self.state == "home":
            self.show_home_screen()
        elif self.state == "song_selection":
            self.song_selection.draw()
        elif self.state == "gameplay":
            # Implement gameplay logic using self.current_beatmap
            pass

    def handle_events(self, event):
        if self.state == "home":
            self.handle_home_screen_events(event)
        elif self.state == "song_selection":
            self.song_selection.handle_event(event)

    def handle_home_screen_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button, position in self.buttons:
                text = self.small_font.render(button, True, (0, 0, 0))
                rect = text.get_rect(center=(self.screen.get_width() // 2, position))
                if rect.collidepoint(event.pos):
                    if button == "Play":
                        self.state = "song_selection"
                    elif button == "Options":
                        print("Options selected")  # Placeholder for options screen
                    elif button == "Exit":
                        pygame.quit()
                        exit()