import pygame
from constants import Game_state, Colors, Fonts, avg, Text
from level import RectSprite
from random import randint

if not pygame.get_init():
    pygame.init()


class LevelButton(RectSprite):
    def __init__(self, width, height, name, group, pos=(0, 0)):
        super().__init__(width, height, color=Colors.LVL_RECT_COLOR)

        self.name = Text(Fonts.BIGGER_FONT, str(name), Colors.TEXT_COLOR)
        stats = Game_state.lvl_stats[self.name.text]
        self.highscore = Text(Fonts.BIGGER_FONT, str(stats[0]), Colors.TEXT_COLOR)
        self.stars = Text(Fonts.STAR_FONT_BIG, stats[1] * '*', Colors.TEXT_COLOR)

        self.rect.topleft = pos

        self.highscore.rect.center = self.rect.center
        tx = self.rect.centerx
        ty = avg(self.rect.top, self.highscore.rect.top)
        self.name.rect.center = (tx,ty)
        ty = avg(self.rect.bottom, self.highscore.rect.bottom)
        self.stars.rect.center = (tx,ty)

        self.hover_color = Colors.LVL_RECT_HOVER_COLOR
        self.normal_color = Colors.LVL_RECT_COLOR

        group.add(self, self.name, self.highscore, self.stars)

    def is_over(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def update(self, mouse_pos):
        stats = Game_state.lvl_stats[self.name.text]
        self.highscore.update_text(stats[0])
        self.stars.update_text(stats[1]*'*')

        self.color = self.normal_color
        if self.is_over(mouse_pos):
            self.color = self.hover_color

        self.image.fill(self.color)


class Menu(RectSprite):
    def __init__(self, width, height, color=Colors.BG_COLOR):
        super().__init__(width, height, color)
        self.lvl_buttons = []
        self.group = pygame.sprite.Group()

        self.title = Text(Fonts.TITLE_FONT, "Level Selection", Colors.TEXT_COLOR)
        self.title.rect.center = (round(Game_state.WIN_W * 0.5), round(Game_state.WIN_H * 0.1))
        self.group.add(self.title)

    def make_rects(self):
        # UPDATE IN CASE STH CHANGED
        self.lvl_buttons = []
        self.group = pygame.sprite.Group()
        self.title.add(self.group)

        # LEVEL COUNT
        LVL_COUNT = len(Game_state.lvl_list)

        # MARGINS
        X_MARGIN = round(Game_state.WIN_W * 0.05)
        Y_MARGIN = round(Game_state.WIN_H * 0.2)

        # GAPS BETWEEN BUTTONS
        X_GAP = round(Game_state.WIN_W * 0.0025)
        Y_GAP = round(Game_state.WIN_H * 0.0025)

        # BUTTONS PER ONE ROW, ONE COLUMN
        BUTTONS_PER_ROW = 3
        BUTTONS_PER_COL = max(round(LVL_COUNT / BUTTONS_PER_ROW), 1)

        # BUTTON WIDTH AND HEIGHT
        BUTTON_W = ((Game_state.WIN_W - 2 * X_MARGIN - ((BUTTONS_PER_ROW - 1) * X_GAP)) // BUTTONS_PER_ROW)
        BUTTON_H = ((Game_state.WIN_H - 2 * Y_MARGIN - ((BUTTONS_PER_COL - 1) * Y_GAP)) // BUTTONS_PER_COL)

        # FIRST BUTTON'S X AND Y COORDINATES
        button_x, button_y = X_MARGIN, Y_MARGIN

        for i in range(LVL_COUNT):
            if i != 0:
                button_x += BUTTON_W + X_GAP

            if i % BUTTONS_PER_ROW == 0 and i != 0:
                button_y += BUTTON_H + Y_GAP
                button_x = X_MARGIN

            lvl = Game_state.lvl_list[i]

            button = LevelButton(BUTTON_W, BUTTON_H, lvl.name, self.group, (button_x, button_y))

            self.lvl_buttons.append(button)


    def update(self):
        # for button in self.lvl_buttons:
        #     button.update(pygame.mouse.get_pos())
        self.group.update(pygame.mouse.get_pos())  # Will be invalid if Text
                                                   # gets an update function


def draw_menu():
    """Basic UI for lvl select aka menu"""
    # Game_state.lvl_rects = []
    Game_state.DISP_SURF.fill(Colors.BG_COLOR)
    Game_state.MENU.update()
    Game_state.MENU.group.draw(Game_state.DISP_SURF)


def draw_drone(Game_state, drone):
    if drone.crate:
        crate_rect = pygame.rect.Rect(0, 0, 32, 32)
        crate_rect.center = drone.crate_sprite.rect.center
        pygame.draw.rect(Game_state.curr_lvl.image, drone.crate, crate_rect)
        Game_state.curr_lvl.image.blit(
            drone.crate_sprite.image, drone.crate_sprite.rect)
    Game_state.curr_lvl.image.blit(drone.image, drone.draw_rect)


def draw_level(Game_state, level, drone):
    Game_state.DISP_SURF.fill(Colors.BG_COLOR)
    Game_state.curr_lvl.image.fill(Colors.LVL_BG_COLOR)
    WIN_W, WIN_H = Game_state.curr_lvl.image.get_size()

    # UI
    txt_group = pygame.sprite.Group()
    txt = Text(Fonts.BASIC_FONT,
               f"Score: {Game_state.score} / {Game_state.curr_lvl.score_to_win}", Colors.TEXT_COLOR)
    txt.rect.topright = (WIN_W - 10, 10)
    txt_group.add(txt)

    txt = Text(Fonts.BASIC_FONT,
               f"Health: {round(Game_state.drone.health) * '|'}", Colors.TEXT_COLOR)
    txt.rect.topleft = (10, 10)
    txt_group.add(txt)

    txt = Text(Fonts.BASIC_FONT,
               f"Time left: {round(level.time_remaining)}", Colors.TEXT_COLOR)
    txt.rect.topright = (WIN_W - 10, 40)
    txt_group.add(txt)

    txt_group.draw(Game_state.curr_lvl.image)

    # Drawing the level
    level.group.update()
    level.group.draw(Game_state.curr_lvl.image)
    draw_drone(Game_state, drone)

    x, y = 0, 0
    if drone.damage > 1:
        dmg = round(drone.damage)
        x = randint(-dmg, dmg)
        y = randint(-dmg, dmg)
        drone.damage *= 0.5
    Game_state.DISP_SURF.blit(resize_levelsurf(), (x, y))


def draw_game_over():
    Game_state.DISP_SURF.fill(Colors.BG_COLOR)
    Game_state.curr_lvl.image.fill(Colors.LVL_BG_COLOR)
    WIN_W, WIN_H = Game_state.curr_lvl.image.get_size()

    txt_group = pygame.sprite.Group()
    txt = Text(Fonts.TITLE_FONT, "GAME OVER!", Colors.TEXT_COLOR)
    txt.rect.midtop = (WIN_W//2, 30)
    txt_group.add(txt)

    if Game_state.drone.health <= 0:
        reason = "Your drone broke down!"

    elif Game_state.score >= Game_state.curr_lvl.min_score_to_win:
        reason = "You completed the level!"

    else:
        reason = "You ran out of time!"

    txt = Text(Fonts.BIGGER_FONT, reason, Colors.TEXT_COLOR)
    txt.rect.midtop = (WIN_W//2, 150)
    txt_group.add(txt)
    txt = Text(Fonts.BIGGER_FONT,
               f"Score: {Game_state.score}", Colors.TEXT_COLOR)
    txt.rect.midtop = (WIN_W//2, 220)
    txt_group.add(txt)
    txt = Text(Fonts.STAR_FONT_BIG,
               f"Rating: {Game_state.curr_lvl.exit_platform.text}", Colors.TEXT_COLOR)
    txt.rect.midtop = (WIN_W//2, 270)
    txt_group.add(txt)
    txt = Text(Fonts.BASIC_FONT,
               "Press SPACE to return to level selection, ESC to quit", Colors.TEXT_COLOR)
    txt.rect.midtop = (WIN_W//2, 360)
    txt_group.add(txt)

    txt_group.draw(Game_state.curr_lvl.image)
    Game_state.DISP_SURF.blit(resize_levelsurf(), (0, 0))


def resize_levelsurf():
    WIN_W, WIN_H = Game_state.curr_lvl.image.get_size()
    REAL_W, REAL_H = Game_state.WIN_W, Game_state.WIN_H
    diff_x, diff_y = REAL_W/WIN_W, REAL_H/WIN_H
    zoom = min(diff_x, diff_y)
    return pygame.transform.smoothscale(Game_state.curr_lvl.image, (int(WIN_W*zoom), int(WIN_H*zoom)))
