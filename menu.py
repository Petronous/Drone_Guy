import pygame
from graphics import Menu


def handle_input(game_state):
    # RETURN THE INDEX OF THE LVL => 0 = LVL 1
    for event in pygame.event.get(pygame.MOUSEBUTTONUP):
        for lvl_rect in Menu.LVL_RECTS:
            if lvl_rect.collidepoint(pygame.mouse.get_pos()):
                return Menu.LVL_RECTS.index(lvl_rect)
