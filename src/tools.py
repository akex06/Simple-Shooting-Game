import pygame

from src.constants import (
    BLACK
)

class Tools:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def draw_score(self, font: pygame.font.Font, amount: int):
        self.screen.blit(font.render(f"Amount {amount}", True, BLACK), (20, 20))