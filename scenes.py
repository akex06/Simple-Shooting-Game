import pygame
import json
import random

from typing import Dict
from src.sprites import Target
from random import randint
from src.tools import Tools

from src.constants import (
    BLACK,
    WHITE
)

with open("src/leaderboard.json") as f:
    lb = json.load(f)

class SceneManager:
    def __init__(self, screen: pygame.Surface, tools: Tools):
        self.screen = screen
        self.scene = "menu"
        self.targets = pygame.sprite.Group()
        self.draw = True
        self.crosshair = pygame.image.load("assets/crosshair.png").convert()
        self.crosshair = pygame.transform.scale(self.crosshair, (120, 120))
        self.crosshair.set_colorkey(WHITE)
        self.amount = 0
        self.font = pygame.font.SysFont("Sans", 60)
        self.tools = tools
        self.buttons: Dict[str, pygame.Rect] = {}
        self.arrow = pygame.transform.scale(pygame.image.load("assets/arrow.png"), (100, 100))
        self.player_name = ""

    def process_game_interaction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.scene == "game":
                    for sprite in self.targets:
                        if sprite.rect.collidepoint(event.pos):
                            self.targets.remove(sprite)
                            self.amount += 1
                            self.tools.draw(self.tools.get_text(f"Amount: {self.amount}", self.font))
    
                if self.scene == "menu":
                    for name, button in self.buttons.items():
                        if button.collidepoint(event.pos):
                            if name.lower() == "play":
                                self.scene = "name"

                            if name.lower() == "leaderboard":
                                self.scene = "leaderboard"
                
                if self.scene == "leaderboard":
                    if self.arrow.get_rect().collidepoint(event.pos):
                        self.scene = "menu"

            if event.type == pygame.KEYDOWN:
                if self.scene == "name":
                    try:
                        if chr(event.key).upper() in [chr(x) for x in range(65, 91)]:
                            self.player_name += chr(event.key)
                        
                        elif event.key == 13 and len(self.player_name) > 3:
                                self.scene = "game"
                            
                        elif event.key == 8:
                            self.player_name = self.player_name[:-1]
                    
                    except:
                        pass        
    def menu(self):
        self.screen.fill(WHITE)
        
        texts = ["Play", "Leaderboard"]
        n = 300
        for text in texts:
            text_surface = self.tools.get_text(text, self.font)
            play_button = self.tools.draw(text_surface, (self.screen.get_width()/2 - text_surface.get_width()/2, n))
            n += 80

            if play_button not in self.buttons.values():
                self.buttons[text] = play_button

    def name(self):
        self.screen.fill(WHITE)

        text = self.tools.get_text("Enter your name", self.font)
        self.tools.draw(text, (self.screen.get_width()/2 - text.get_width()/2, 200))

        text = self.tools.get_text(self.player_name, self.font)
        self.tools.draw(text, (self.screen.get_width()/2 - text.get_width()/2 ,280))


    def game(self):
        self.screen.fill(WHITE)
        self.tools.draw(self.tools.get_text(f"Amount: {self.amount}", self.font))

        if self.draw:
            for i in range(20):
                target = Target()
                target.rect.x = random.randint(0, self.screen.get_width()-self.crosshair.get_width())
                target.rect.y = random.randint(0, self.screen.get_height()-self.crosshair.get_height())

                self.targets.add(target)
        
            self.draw = False

        self.targets.draw(self.screen)

        if len(self.targets)  == 0:
            self.draw = True

        mouse = pygame.mouse.get_pos()
        crosshair_pos = (mouse[0] - self.crosshair.get_width()/2, mouse[1] - self.crosshair.get_height()/2)

        pygame.mouse.set_visible(False)

        self.screen.blit(self.crosshair, crosshair_pos)

    def leaderboard(self):
        self.screen.fill(WHITE)

        self.screen.blit(self.arrow, (20, 20))