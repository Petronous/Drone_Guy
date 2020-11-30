import pygame
from game_state import Game_state

def handle_input():
    """Return the index of the lvl the user has chosen by clicking on it's rect (=> 0 = LVL 1), if nothing was chosen returns None"""
    for event in pygame.event.get(pygame.MOUSEBUTTONUP):
        for lvl_rect in Game_state.lvl_rects:
            if lvl_rect.rect.collidepoint(pygame.mouse.get_pos()):
                return Game_state.lvl_rects.index(lvl_rect)
