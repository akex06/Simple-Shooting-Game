import pygame

from typing import Tuple

from src.constants import (
    BLACK
)

class Tools:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def get_text(self, text: str, font: pygame.font.Font, color: Tuple[int] = BLACK):
        return font.render(text, True, color)

    def draw(self, text: pygame.Surface, coords: Tuple[int] = (20, 20)):
        return self.screen.blit(text, coords)