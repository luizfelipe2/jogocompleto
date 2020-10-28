import pygame
import math

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/inimigo.png")
        self.image = pygame.transform.scale(self.image, [40, 35])
        self.rect = pygame.Rect(780, 350, 50, 50)


        self.timer = 0
    def update(self, *args):
        self.timer += 0.05
        self.rect.y = 380 + math.sin(self.timer) * 70