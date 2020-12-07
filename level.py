import pygame
from random import choice
from constants import Colors, Game_state


class Rect_sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Level():
    def __init__(self, blocks=[], spawners=[], drone_start_pos=(0, 0), time_remaining=60):
        self.blocks = blocks
        self.spawners = spawners
        self.drone_start_pos = drone_start_pos
        self.group = pygame.sprite.Group()
        self.time_remaining = time_remaining
        Game_state.lvl_list.append(self)


class Block(Rect_sprite):
    def __init__(self, x, y, width, height, group):
        super().__init__(width, height, (150, 150, 150))
        self.rect.topleft = (x, y)
        group.add(self)


class Spawner(Rect_sprite):
    def __init__(self, x, y, width, height, color, group):
        super().__init__(width, height, color)
        self.detector = pygame.Rect(x, y, 40, 40)
        self.rect.midtop = self.detector.midbottom
        self.color = color
        self.crate = False
        self.crate_cd = 0
        group.add(self)
        Game_state.spawners.append(self)

    def update(self):
        self.crate_color = Colors.BG_COLOR

        if not self.crate:
            self.crate_cd -= Game_state.FPS_CLOCK.get_time() / 1000
            if self.crate_cd <= 0:
                destinations = Game_state.spawners.copy()
                destinations.remove(self)

                self.crate_destination = choice(destinations)
                self.crate = True

        if self.crate:
            self.crate_color = self.crate_destination.color
            self.crate_cd = 5

        pygame.draw.rect(Game_state.DISP_SURF, self.crate_color, self.detector)
