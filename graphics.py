import pygame
from constants import Game_state, Colors, Fonts
from level import RectSprite
from random import randint

if not pygame.get_init():
    pygame.init()


class Text(pygame.sprite.Sprite):
    """Creates a sprite containing the text"""

    def __init__(self, font, text, color):
        super().__init__()
        self.image = font.render(
            text, True, color)
        self.rect = self.image.get_rect()


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

    for i in range(LVL_COUNT):
        if i != 0:
            lvl_rect_x += LVL_RECT_W + GAP_W

        if i % RECTS_PER_ROW == 0 and i != 0:
            lvl_rect_y += LVL_RECT_H + GAP_H
            lvl_rect_x = X_MARGIN

        lvl_rect = RectSprite(LVL_RECT_W, LVL_RECT_H, Colors.LVL_RECT_COLOR)
        lvl_rect.rect.topleft = (lvl_rect_x, lvl_rect_y)
        Game_state.DISP_SURF.blit(lvl_rect.image, lvl_rect.rect)

        lvl = Game_state.lvl_list[i]
        lvl_num = Text(Fonts.BIGGER_FONT, lvl.name, Colors.TEXT_COLOR)
        highscore = Text(Fonts.BIGGER_FONT, str(Game_state.lvl_stats[lvl.name][0]), Colors.TEXT_COLOR)
        stars = Text(Fonts.STAR_FONT_BIG, Game_state.lvl_stats[lvl.name][1]*'*', Colors.TEXT_COLOR)

        highscore.rect.midtop = lvl_num.rect.midbottom
        text_rect = lvl_num.rect.union(highscore.rect)
        stars.rect.midtop = highscore.rect.midbottom
        text_rect = text_rect.union(stars.rect)
        text_rect.center = lvl_rect.rect.center

        text_surf = pygame.Surface(text_rect.size)
        text_surf.fill(Colors.LVL_RECT_COLOR)
        text_surf.blits([(x.image, x.rect) for x in (lvl_num, highscore, stars)])
        Game_state.DISP_SURF.blit(text_surf, text_rect)

        Game_state.lvl_rects.append(lvl_rect)

    MENU_GRP.draw(Game_state.DISP_SURF)


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
               f"Health: {round(Game_state.drone.health)}", Colors.TEXT_COLOR)
    txt.rect.topright = (WIN_W - 10, 40)
    txt_group.add(txt)
    txt = Text(Fonts.BASIC_FONT,
               f"Remaining time: {round(level.time_remaining)}", Colors.TEXT_COLOR)
    txt.rect.topright = (WIN_W - 10, 70)
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
    REAL_W, REAL_H = Game_state.DISP_SURF.get_size()
    diff_x, diff_y = REAL_W/WIN_W, REAL_H/WIN_H
    zoom = min(diff_x, diff_y)
    return pygame.transform.smoothscale(Game_state.curr_lvl.image, (int(WIN_W*zoom), int(WIN_H*zoom)))
