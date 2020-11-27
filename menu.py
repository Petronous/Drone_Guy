import pygame
from graphics import Menu


def handle_input(game_state):
    """Return the index of the lvl the user has chosen by clicking on it's rect (=> 0 = LVL 1), if nothing was chosen returns None"""
    for event in pygame.event.get(pygame.MOUSEBUTTONUP):
        for lvl_rect in Menu.LVL_RECTS:
            if lvl_rect.collidepoint(pygame.mouse.get_pos()):
                return Menu.LVL_RECTS.index(lvl_rect)
