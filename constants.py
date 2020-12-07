import pygame


class Game_state():
    """Most of the info any other file would need to use from main.py"""
    DISP_SURF = None
    FPS_CLOCK = None
    room = "menu"
    drone = None
    lvl_list = []
    lvl_rects = []
    curr_lvl = None
    score = 0


class Colors():
    """Contains used colors"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    GREEN = (0, 255, 0)
    BG_COLOR = BLACK
    LVL_BG_COLOR = (50, 50, 50)
    LVL_RECT_COLOR = GREEN
    TEXT_COLOR = WHITE
    DRONE_COLOR = GRAY
