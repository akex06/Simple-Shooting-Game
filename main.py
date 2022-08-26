import pygame

from src.scenes import SceneManager
from src.tools import Tools

pygame.init()

def main_loop(game_controller: SceneManager, screen: pygame.Surface, clock: pygame.time.Clock):
    quit_game: bool = False

    while not quit_game:
        screen.fill(BLACK)
        quit_game = game_controller.process_game_interaction()

        scene = getattr(game_controller, game_controller.scene)()

        pygame.display.update()
        clock.tick(FRAME_RATE)

if __name__ == "__main__":
    from src.constants import (
        BLACK,
        MIN_WIN_WIDTH,
        MIN_WIN_HEIGHT,
        FRAME_RATE
    )

    flags = pygame.FULLSCREEN | pygame.SCALED
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((MIN_WIN_WIDTH, MIN_WIN_HEIGHT), flags = flags)
    
    tools = Tools(screen)
    game_controller = SceneManager(screen, tools)
    
    main_loop(game_controller, screen, clock)
    
    exit()