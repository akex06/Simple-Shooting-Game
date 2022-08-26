import pygame

from src.constants import (
    WHITE
)

class Target(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/target.png").convert()
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()