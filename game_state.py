import pygame
import levels

class Game_state():
    """Most of the info any other file would need to use from main.py"""
    DISP_SURF = None
    room = "menu"
    drone = None
    obstacles = []
    spawners = []
    lvl_list = levels.lvl_list
    lvl_rects = []
    curr_lvl = None
    score = 0
