import pygame
import math

class Tiro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/tiro.png")
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = self.image.get_rect()

        self.speed = 5

    def update(self, *args):
        #direcao do tiro
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            if self.rect.bottom > 600:
                self.kill()

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            if self.rect.right < 0:
                self.kill()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            if self.rect.top < 0:
                self.kill()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            if self.rect.left > 920:
                self.kill()
