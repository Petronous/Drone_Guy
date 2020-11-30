import pygame
from constants import Colors


class Rect_sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Level():
    def __init__(self, blocks=[], spawners=[], drone_start_pos=(0, 0)):
        self.blocks = blocks
        self.spawners = spawners
        self.drone_start_pos = drone_start_pos
        self.group = pygame.sprite.Group()


class Block(Rect_sprite):
    def __init__(self, x, y, width, height, group):
        super().__init__(width, height, (150, 150, 150))
        self.rect.topleft = (x, y)
        group.add(self)


"""
    Is this necessary?

    def draw(self, surf):
        surf.blit(self.image, self.rect)
"""


class Spawner(Rect_sprite):
    def __init__(self, x, y, width, height, color, group):
        super().__init__(width, height, color)
        self.detector = pygame.Rect(x, y, 40, 40)
        self.rect.midtop = self.detector.midbottom
        self.color = color
        group.add(self)


"""
    Same here

    def draw(self, surf):
        surf.blit(self.image, self.rect)
"""
