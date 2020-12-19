import pygame
from constants import Game_state
from levels import RectSprite


def sign(a): return 1 if a > 0 else -1 if a < 0 else 0


def get_bigger(a, b):
    if a >= b:
        return a, 1
    else:
        return b, -1


def get_coll_side(leftdist, rightdist, topdist, bottomdist):
    dist_x, drc_x = get_bigger(leftdist, rightdist)
    dist_y, drc_y = get_bigger(topdist, bottomdist)

    dist, x_or_y = get_bigger(dist_y, dist_x)
    x_or_y = (x_or_y + 1) // 2
    drcs = (drc_x, drc_y)
    return x_or_y, drcs, dist


def clamp_vel(vel, mx):
    if abs(vel) > mx:
        vel = sign(vel)*mx


class Drone(pygame.sprite.Sprite):
    """docstring for Drone."""

    def __init__(self, x=0, y=0):
        super(Drone, self).__init__()
        self.rect = pygame.Rect(x, y, 80, 50)
        self.draw_rect = pygame.Rect(0, 0, 100, 60)
        self.draw_rect.midbottom = self.rect.midbottom
        self.image = pygame.image.load("imgs/drone.png")
        self.image = pygame.transform.smoothscale(
            self.image, self.draw_rect.size)
        self.crate_sprite = RectSprite(36, 36, image_path="imgs/crate.png")
        self.crate_sprite.rect.midbottom = self.rect.midbottom
        self.vel = [0, 0]
        self.v_acc = 0.3
        self.h_acc = 0.6
        self.gravity = 0.3
        self.pos_x = 0
        self.pos_y = 0
        self.control_v = 0
        self.control_h = 0

        self.max_spd = 15
        self.durability = 5
        self.health = 100
        self.crate = None

    def update(self):
        # update velocity based on gravity and controls
        self.vel[0] += self.h_acc * self.control_h
        self.vel[1] += (self.v_acc + self.gravity) * \
            self.control_v + self.gravity

        self.rect.center = (int(self.pos_x), int(self.pos_y))

        # detect collision
        self.collide_level_boundaries(Game_state.curr_lvl.rect)
        for obstacle in Game_state.curr_lvl.blocks:
            if self.rect.colliderect(obstacle.rect):
                self.collide_box(obstacle.rect)
        for spawner in Game_state.curr_lvl.spawners:
            if self.rect.colliderect(spawner.rect):
                self.collide_box(spawner.rect)
            if self.rect.collidepoint(spawner.detector.midbottom) and self.vel[0] <= 10:
                if self.crate is None and spawner.crate:
                    self.crate = spawner.crate_color
                    spawner.crate = False
                elif self.crate == spawner.color:
                    self.crate = None
                    Game_state.score += 1

        self.pos_x += self.vel[0]
        self.pos_y += self.vel[1]
        self.rect.center = (int(self.pos_x), int(self.pos_y))
        self.draw_rect.midbottom = self.rect.midbottom
        self.crate_sprite.rect.midbottom = self.rect.midbottom

    def collide_level_boundaries(self, other):
        x_or_y, drcs, dist = get_coll_side(self.rect.right - other.right, other.left - self.rect.left,
                                           self.rect.bottom - other.bottom, other.top - self.rect.top)
        if dist > 0:
            self.collide(x_or_y, drcs)

    def collide_box(self, other):
        '''
        Handles collision
        '''
        x_or_y, drcs, _ = get_coll_side(other.left - self.rect.right, self.rect.left - other.right,
                                        other.top - self.rect.bottom, self.rect.top - other.bottom)
        self.collide(x_or_y, drcs)

    def collide(self, x_or_y, drcs):
        impact_vel = self.vel[x_or_y]*drcs[x_or_y]
        self.vel[(x_or_y+1) % 2] *= 0.9  # To simulate friction

        if impact_vel > 0:
            # check for damage if bump
            if impact_vel > self.durability:
                self.health -= (impact_vel - self.durability)*1.35
            self.vel[x_or_y] = 0
