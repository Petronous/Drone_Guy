import pygame
from constants import Game_state, Colors
from level import Rect_sprite

if not pygame.get_init():
    pygame.init()


class Text(pygame.sprite.Sprite):
    """Creates a sprite containing the text"""

    def __init__(self, font, text, color):
        super().__init__()
        self.image = font.render(
            text, True, color)
        self.rect = self.image.get_rect()


class Fonts():
    """Basic fonts"""
    BASE_FONT_SIZE = 20
    TITLE_FONT_SIZE = 4 * BASE_FONT_SIZE
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASE_FONT_SIZE)
    TITLE_FONT = pygame.font.Font('freesansbold.ttf', TITLE_FONT_SIZE)


class Menu():
    """Class to be passed to handle_input() in menu.py for lvl selection"""
    LVL_RECTS = []


def draw_menu():
    """Scrappy and sloppy basic graphics for lvl select aka menu"""
    # GET WINDOW DIMENSIONS
    WIN_W, WIN_H = Game_state.DISP_SURF.get_size()

    Game_state.lvl_rects = []

    # FILL THE WINDOW WITH BG_COLOR
    Game_state.DISP_SURF.fill(Colors.BG_COLOR)

    # LVL SELECT TEXT
    LVL_SELECT = Text(
        Fonts.TITLE_FONT, "Level selection", Colors.TEXT_COLOR)
    LVL_SELECT.rect.midtop = (WIN_W * 0.5, WIN_H * 0.05)

    # CREATE MENU SPRITE GROUP
    MENU_GRP = pygame.sprite.Group()
    MENU_GRP.add(LVL_SELECT)

    # EVERYTHING AFTER THIS COMMENT SHOULD BE REVISITED
    X_MARGIN = WIN_W * 0.025
    Y_MARGIN = WIN_H * 0.2
    GAP_W = 0.0025 * WIN_W
    GAP_H = 0.0025 * WIN_H
    LVL_COUNT = len(Game_state.lvl_list)
    RECTS_PER_ROW = 5
    LVL_RECT_W = (WIN_W - 2 * X_MARGIN - (LVL_COUNT - 1)
                  * GAP_W) // RECTS_PER_ROW
    LVL_RECT_H = (WIN_H - 2 * Y_MARGIN - (LVL_COUNT - 1)
                  * GAP_H) // (LVL_COUNT + 1 // RECTS_PER_ROW)

    lvl_rect_x, lvl_rect_y = X_MARGIN, Y_MARGIN

    for i in range(1, LVL_COUNT+1):
        if (i - 1) != 0:
            lvl_rect_x += LVL_RECT_W + GAP_W

        if (i - 1) % RECTS_PER_ROW == 0 and (i - 1) != 0:
            lvl_rect_y += LVL_RECT_H + GAP_H
            lvl_rect_x = X_MARGIN

        lvl_rect = Rect_sprite(LVL_RECT_W, LVL_RECT_H, Colors.LVL_RECT_COLOR)
        lvl_rect.rect.topleft = (lvl_rect_x, lvl_rect_y)
        MENU_GRP.add(lvl_rect)

        lvl_num = Text(Fonts.BASIC_FONT, str(i), Colors.TEXT_COLOR)
        lvl_num.rect.center = lvl_rect.rect.center
        MENU_GRP.add(lvl_num)

        Game_state.lvl_rects.append(lvl_rect)

    MENU_GRP.draw(Game_state.DISP_SURF)


def draw_drone(Game_state, drone):
    pygame.draw.rect(Game_state.curr_lvl.image, Colors.DRONE_COLOR, drone.rect)
    if drone.crate:
        crate_rect = pygame.rect.Rect(0,0,40,40)
        crate_rect.midbottom = drone.rect.midbottom
        pygame.draw.rect(Game_state.curr_lvl.image, drone.crate, crate_rect)


def draw_level(Game_state, level, drone):
    Game_state.DISP_SURF.fill(Colors.BG_COLOR)
    Game_state.curr_lvl.image.fill(Colors.LVL_BG_COLOR)
    WIN_W, WIN_H = Game_state.curr_lvl.image.get_size()

    # UI
    txt_group = pygame.sprite.Group()
    txt = Text(Fonts.BASIC_FONT, "Score: " + str(Game_state.score), Colors.TEXT_COLOR)
    txt.rect.topright = (WIN_W - 10, 10)
    txt_group.add(txt)
    txt = Text(Fonts.BASIC_FONT, "Health: " + str(round(Game_state.drone.health)), Colors.TEXT_COLOR)
    txt.rect.topright = (WIN_W - 10, 40)
    txt_group.add(txt)
    txt = Text(Fonts.BASIC_FONT, "Remaining time: " + str(round(level.time_remaining)), Colors.TEXT_COLOR)
    txt.rect.topright = (WIN_W - 10, 70)
    txt_group.add(txt)

    txt_group.draw(Game_state.curr_lvl.image)

    # Drawing the level
    level.group.update()
    draw_drone(Game_state, drone)
    level.group.draw(Game_state.curr_lvl.image)
    surfgroup = pygame.sprite.Group()
    surfgroup.add(level)
    surfgroup.draw(Game_state.DISP_SURF)
