import pygame
from random import choice
from constants import Colors, Game_state, Fonts, Text, RectSprite


class Level(RectSprite):
    def __init__(self, name, drone_start_pos=(100, 100), time_remaining=60, star_points = [8], size=(1728, 972)):
        super().__init__(size[0], size[1], Colors.LVL_BG_COLOR)
        self.name = str(name)
        self.blocks = []
        self.spawners = []
        self.labels = []
        self.exit_platform = None
        self.drone_start_pos = drone_start_pos
        self.group = pygame.sprite.Group()
        self.init_time = time_remaining
        self.time_remaining = time_remaining
        self.star_ratings = star_points
        star_points.append(star_points[-1])
        self.min_score_to_win = star_points[0]
        self.star_points = iter(star_points)
        self.score_to_win = next(self.star_points)
        Game_state.lvl_list.append(self)

    def new_label(self, x, y, font, text, color):
        label = Text(font, text, color)
        label.rect.topleft = (x,y)
        label.add(self.group)

    def new_block(self, x, y, width, height):
        self.blocks.append(Block(x, y, width, height, self.group))

    def new_spawner(self, x, y, width, height, color):
        self.spawners.append(
            Spawner(x, y, width, height, color, self.group))

    def end_level(self):
        self.time_remaining = 0

    def make_exit_platform(self, x, y, width, height):
        self.exit_platform = Platform(x, y, width, height, self.group, self.end_level, Colors.FINISH_GREEN, Colors.GRAY)
        self.blocks.append(self.exit_platform)

    def setup(self):
        Game_state.curr_lvl.time_remaining = Game_state.curr_lvl.init_time
        Game_state.curr_lvl.exit_platform.activated = False
        Game_state.curr_lvl.exit_platform.text = ""

        for spawner in Game_state.curr_lvl.spawners:
            spawner.crate = False
            spawner.crate_cd = 0

        Game_state.curr_lvl.star_points = iter(Game_state.curr_lvl.star_ratings)
        Game_state.curr_lvl.score_to_win = next(Game_state.curr_lvl.star_points)


class Block(RectSprite):
    def __init__(self, x, y, width, height, group):
        super().__init__(width, height, color = Colors.GRAY)
        self.rect.topleft = (x, y)
        group.add(self)


class Platform(RectSprite):
    def __init__(self, x, y, w, h, group, on_hit, on_color, off_color, max_vel = 1, text = "", text_color = Colors.WHITE):
        super().__init__(w, h, color = off_color)
        self.rect.topleft = (x, y)
        self.on_color = on_color
        self.off_color = off_color
        self.color = off_color
        self.activated = False
        self.on_hit = on_hit
        self.max_vel = max_vel
        self.text = text
        self.label = Text(Fonts.STAR_FONT, text, text_color)
        self.label.rect.center = self.rect.center
        self.update_label()
        group.add(self, self.label)

    def update(self):
        if self.activated:
            if self.color != self.on_color:
                self.image.fill(self.on_color)
                self.color = self.on_color
                self.update_label()
            if self.rect.collidepoint(Game_state.drone.rect.midbottom):
                if max(map(abs, Game_state.drone.vel)) <= self.max_vel:
                    self.on_hit()

        elif self.color != self.off_color:
            self.image.fill(self.off_color)
            self.color = self.off_color
            self.update_label()

    def update_label(self):
        print(self.text, self.label.text)
        self.label.update_text(self.text)


class Spawner(RectSprite):
    def __init__(self, x, y, width, height, color, group):
        super().__init__(width, height, color = color)
        self.detector = pygame.Rect(x, y, 40, 40)
        self.color_rect = pygame.Rect(0, 0, 36, 36)
        self.rect.midtop = self.detector.midbottom
        self.color_rect.center = self.detector.center
        self.color = color
        self.crate_sprite = RectSprite(40, 40, image_path = "imgs/crate.png")
        self.crate_sprite.rect = self.detector
        group.add(self.crate_sprite)
        self.crate = False
        self.crate_cd = 0
        group.add(self)

    def update(self):
        self.crate_color = Colors.LVL_BG_COLOR

        if not self.crate:
            if self.crate_sprite.alive(): self.crate_sprite.kill()
            self.crate_cd -= Game_state.FPS_CLOCK.get_time() / 1000
            if self.crate_cd <= 0:
                destinations = Game_state.curr_lvl.spawners.copy()
                destinations.remove(self)

                self.crate_destination = choice(destinations)
                self.crate_sprite.add(Game_state.curr_lvl.group)
                self.crate = True

        if self.crate:
            self.crate_color = self.crate_destination.color
            self.crate_cd = 10

        pygame.draw.rect(Game_state.curr_lvl.image,
                         self.crate_color, self.color_rect)
