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
        self.rect.center = (int(self.pos_x), int(self.pos_y))

    def collide(self, other):
        '''
        Handles collision
        '''
        dist_x, drc_x = get_bigger(other.rect.left - self.rect.right, self.rect.left - other.rect.right)
        dist_y, drc_y = get_bigger(other.rect.top - self.rect.bottom, self.rect.top - other.rect.bottom)

        dist, x_or_y = get_bigger(dist_y, dist_x)
        x_or_y = (x_or_y + 1) // 2
        drcs = (drc_x, drc_y)

        impact_vel = self.vel[x_or_y]*drcs[x_or_y]
        self.vel[(x_or_y+1)%2] *= 0.9  # To simulate friction

        if impact_vel > 0:
            # check for damage if bump
            if impact_vel > self.durability:
                self.health -=  impact_vel - self.durability
            self.self.vel[x_or_y] = 0
