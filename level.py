import pygame

class Rect_sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Level():
    def __init__(self, blocks=[], spawners=[]):
        self.blocks = blocks
        self.spawners = spawners
        self.group = pygame.sprite.Group()


class Block(Rect_sprite):
    def __init__(self, x, y, width, height, group, color):
        super().__init__(width, height, color)
        self.pos = (x, y)
        group.add(self)

    def draw(surf):
        surf.blit(self.image, self.rect)
