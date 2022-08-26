import pygame
import random

from src.sprites import Target
from random import randint
from src.tools import Tools

from src.constants import (
    WHITE
)

class SceneManager:
    def __init__(self, screen: pygame.Surface, tools: Tools):
        self.screen = screen
        self.scene = "game"
        self.sprites = pygame.sprite.Group()
        self.draw = True
        self.crosshair = pygame.image.load("assets/crosshair.png").convert()
        self.crosshair = pygame.transform.scale(self.crosshair, (120, 120))
        self.crosshair.set_colorkey(WHITE)
        self.amount = 0
        self.font = pygame.font.SysFont("Sans", 50)
        self.tools = tools
    
    def process_game_interaction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if self.scene == "game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for sprite in self.sprites:
                        if sprite.rect.collidepoint(event.pos):
                            self.sprites.remove(sprite)
                            self.amount += 1
                            self.tools.draw_score(self.font, self.amount)

    def game(self):
        self.screen.fill(WHITE)
        self.tools.draw_score(self.font, self.amount)

        if self.draw:
            for i in range(20):
                target = Target()
                target.rect.x = random.randint(0, self.screen.get_width()-self.crosshair.get_width())
                target.rect.y = random.randint(0, self.screen.get_height()-self.crosshair.get_height())

                self.sprites.add(target)
        
            self.draw = False

        self.sprites.draw(self.screen)

        if len(self.sprites)  == 0:
            self.draw = True

        mouse = pygame.mouse.get_pos()
        crosshair_pos = (mouse[0] - self.crosshair.get_width()/2, mouse[1] - self.crosshair.get_height()/2)

        pygame.mouse.set_visible(False)

        self.screen.blit(self.crosshair, crosshair_pos)