import pygame
from graphics import Rect_sprite


class Level():
    def __init__(self, blocks, spawners, destinations):
        self.blocks = blocks
        self.spawners = spawners
        self.destinations = destinations
        self.group = pygame.sprite.Group()


class Block(Rect_sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.pos = (x, y)
