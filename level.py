import pygame
from graphics import Rect_sprite, Colors


class Level():
    def __init__(self, blocks=[], spawners=[]):
        self.blocks = blocks
        self.spawners = spawners
        self.group = pygame.sprite.Group()


class Block(Rect_sprite):
    def __init__(self, x, y, width, height, group):
        super().__init__(x, y, width, height, (100, 100, 100))
        group.add(self)

    def draw(self, surf):
        surf.blit(self.image, self.rect)


class Spawner(Rect_sprite):
    def __init__(self, width, height, color):
        super().__init__(width, height, Colors.BG_COLOR)
