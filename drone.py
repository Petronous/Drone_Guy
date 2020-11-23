import pygame


def get_bigger(a,b):
    if a >= b:
        return a, 1
    else:
        return b, -1


class Drone(pygame.sprite.Sprite):
    """docstring for Drone."""

    def __init__(self, x = 0, y = 0):
        super(Drone, self).__init__()
        self.rect = pygame.Rect(x,y, 80, 50)
        self.vel = (0,0)
        self.acc = 1
        self.gravity = 1
        self.pos_x = 0
        self.pos_y = 0
        self.control_v = 0
        self.control_h = 0

        self.durability = 10
        self.health = 100
        self.crate  = None

    def update(self, game_state):
        # update velocity based on gravity and controls
        self.vel[0] = self.acc * self.control_h
        self.vel[1] = (self.acc + gravity) * self.control_v + self.gravity

        # detect collision
        for obstacle in game_state.obstacles:
            if self.rect.collideRect(obstacle.rect):
                self.collide(obstacle.rect)
        for spawner in game_state.spawners:
            if self.rect.collideRect(spawner.rect):
                self.collide(spawner.rect)

        self.pos_x += self.vel[0]
        self.pos_y += self.vel[1]
        self.rect.center = (self.pos_x, self.pos_y)

    def collide(self, other):
        '''
        Handles collision
        '''
        left_x, top_y = other.topleft
        right_x, bottom_y = other.bottomright

        dist_x, drc_x = get_bigger(left_x - self.pos_x, self.pos_x - right_x)
        dist_y, drc_y = get_bigger(top_y - self.pos_y, self.pos_y - bottom_y)
        if dist_x > 0 and dist_y > 0:
            dist, x_or_y = get_bigger(dist_x, dist_y)
        # will actually be the index of the smaller one if we take (x,y)
        x_or_y = (x_or_y + 1) // 2
        drcs = (drc_x, drc_y)
        vel = self.vel[x_or_y]*drcs[x_or_y]

        if vel > 0:
            # check for damage if bump
            if vel > self.durability:
                self.health -=  vel - self.durability
            self.self.vel[x_or_y] = 0
