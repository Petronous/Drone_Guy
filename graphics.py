import pygame
pygame.init()


class Colors():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    GREEN = (0, 255, 0)
    BG_COLOR = BLACK
    TEXT_COLOR = WHITE


class Fonts():
    BASE_FONT_SIZE = 20
    TITLE_FONT_SIZE = 4 * BASE_FONT_SIZE
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASE_FONT_SIZE)
    TITLE_FONT = pygame.font.Font('freesansbold.ttf', TITLE_FONT_SIZE)


class Menu():
    LVL_RECTS = []


def draw_menu(game_state):
    # GET WINDOW DIMENSIONS
    WIN_W, WIN_H = game_state.DISPLAY_SURFACE.get_size()

    # FILL THE WINDOW WITH BG_COLOR
    game_state.DISPLAY_SURFACE.fill(Colors.BG_COLOR)

    # CREATE TEXT
    title_surf = Fonts.TITLE_FONT.render(
        "Level selection", True, Colors.TEXT_COLOR)
    title_rect = title_surf.get_rect()

    # CHANGE TEXT'S POS
    title_rect.center = (WIN_W * 0.5, WIN_W * 0.05)

    # DRAW THE TEXT
    game_state.DISPLAY_SURFACE.blit(title_surf, title_rect)

    X_MARGIN = WIN_W * 0.025
    Y_MARGIN = WIN_H * 0.2
    GAP_W = 0.0025 * WIN_W
    GAP_H = 0.0025 * WIN_H
    LVL_COUNT = len(game_state.lvl_list)
    LVL_RECT_W = (WIN_W - 2 * X_MARGIN - (LVL_COUNT - 1) * GAP_W) // 5
    LVL_RECT_H = (WIN_H - 2 * Y_MARGIN - (LVL_COUNT - 1) * GAP_H) // 4

    lvl_rect_x, lvl_rect_y = X_MARGIN, Y_MARGIN
    count = 0

    for i in range(1, LVL_COUNT+1):
        if count != 0:
            lvl_rect_x += LVL_RECT_W + GAP_W

        if count % 5 == 0 and count != 0:
            lvl_rect_y += LVL_RECT_H + GAP_H
            lvl_rect_x = X_MARGIN

        lvl_rect = pygame.draw.rect(
            game_state.DISPLAY_SURFACE, Colors.GREEN, (lvl_rect_x, lvl_rect_y, LVL_RECT_W, LVL_RECT_H))

        game_state.lvl_rects.append(lvl_rect)

        lvl_num_surf = Fonts.BASIC_FONT.render(str(i), True, Colors.WHITE)
        lvl_num_rect = lvl_num_surf.get_rect()

        lvl_num_rect.center = lvl_rect.center

        game_state.DISPLAY_SURFACE.blit(lvl_num_surf, lvl_num_rect)
        count += 1
        Menu.LVL_RECTS.append(lvl_rect)
