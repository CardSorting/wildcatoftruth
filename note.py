import pygame

# Constants
CIRCLE_RADIUS = 50
WHITE = (255, 255, 255)
TIMING_WINDOWS = {
    "Perfect": 50,
    "Great": 100,
    "Good": 150,
    "Bad": 200
}

class Note:
    def __init__(self, x, y, lane_index):
        self.x = x
        self.y = y
        self.radius = CIRCLE_RADIUS
        self.lane_index = lane_index
        self.hit = False

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def update(self):
        self.y += 5  # NOTE_SPEED

    def check_hit(self, y_position):
        if not self.hit:
            timing_error = abs(self.y - y_position)
            if timing_error <= TIMING_WINDOWS["Perfect"]:
                self.hit = "Perfect"
            elif timing_error <= TIMING_WINDOWS["Great"]:
                self.hit = "Great"
            elif timing_error <= TIMING_WINDOWS["Good"]:
                self.hit = "Good"
            elif timing_error <= TIMING_WINDOWS["Bad"]:
                self.hit = "Bad"
            else:
                self.hit = "Miss"
            return self.hit
        return None