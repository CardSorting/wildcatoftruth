import pygame
from note import Note

# Constants
CIRCLE_RADIUS = 50
HIT_POSITION = 550
TIMING_WINDOWS = {
    "Perfect": 50,
    "Great": 100,
    "Good": 150,
    "Bad": 200
}
HIT_EFFECT_DURATION = 300

hit_messages = []

class Lane:
    def __init__(self, x, lane_index, key):
        self.x = x
        self.lane_index = lane_index
        self.notes = []
        self.pressed = False
        self.key = key
        self.hit_effect_time = 0
        self.hit_feedback = ""

    def spawn_note(self):
        note = Note(self.x + CIRCLE_RADIUS, 0, self.lane_index)
        self.notes.append(note)

    def update(self):
        global combo
        for note in self.notes:
            note.update()
            if note.y > HIT_POSITION + TIMING_WINDOWS["Bad"] and not note.hit:
                note.hit = "Miss"
                combo = 0
                hit_messages.append(("Miss", pygame.time.get_ticks(), note.x + CIRCLE_RADIUS))
        self.notes = [note for note in self.notes if not note.hit or note.y <= 600]

    def draw(self, screen):
        for note in self.notes:
            note.draw(screen)

    def check_hits(self, key):
        global score, combo
        current_time = pygame.time.get_ticks()
        if key == self.key:
            self.pressed = True
            for note in self.notes:
                hit_type = note.check_hit(HIT_POSITION)
                if hit_type:
                    pygame.mixer.Sound('/mnt/data/hit_sound.wav').play()
                    if hit_type != "Miss":
                        score += {"Perfect": 100, "Great": 75, "Good": 50, "Bad": 25}[hit_type]
                        combo += 1
                        self.hit_effect_time = current_time
                        self.hit_feedback = hit_type
                        hit_messages.append((hit_type, current_time, note.x + CIRCLE_RADIUS))
                    break

    def release(self, key):
        if key == self.key:
            self.pressed = False