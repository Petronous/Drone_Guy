import pygame
from graphics import Rect_sprite


class Level():
    def __init__(self, blocks=[], spawners=[]):
        self.blocks = blocks
        self.spawners = spawners
        self.group = pygame.sprite.Group()


class Block(Rect_sprite):
    def __init__(self, x, y, width, height):
        super().__init__(width, height, (100, 100, 100))
        self.pos = (x, y)


# BLOCKS
test_blocks = []
test_blocks.append(Block(100, 50, 30, 200))

# LVL
test = Level(test_blocks)


lvl_list = []
lvl_list.append(test)
