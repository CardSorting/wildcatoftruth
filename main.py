import pygame
from game import Game

def main():
    pygame.init()

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Screen setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Osu!mania Clone")

    # Clock to control the frame rate
    clock = pygame.time.Clock()

    # Initialize the game state manager
    game = Game(screen)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_events(event)

        game.update()  # Update the game state

        pygame.display.flip()
        clock.tick(60)  # Maintain 60 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()