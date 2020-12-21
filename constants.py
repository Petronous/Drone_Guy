import pygame
pygame.font.init()

class Game_state():
    """Most of the info any other file would need to use from main.py"""
    DISP_SURF = None
    FPS_CLOCK = None
    room = "menu"
    drone = None
    lvl_list = []
    curr_lvl = None
    score = 0
    lvl_stats = {}
    WIN_W = None
    WIN_H = None
    MENU = None
    lvl_UI_group = None

    @classmethod
    def add_score(cls, score = 1):
        cls.score += score
        if cls.score >= cls.curr_lvl.score_to_win:
            if cls.curr_lvl.exit_platform is not None:
                cls.curr_lvl.exit_platform.activated = True
            while cls.score >= cls.curr_lvl.score_to_win:
                try:
                    cls.curr_lvl.score_to_win = next(cls.curr_lvl.star_points)
                    cls.curr_lvl.exit_platform.text += '*'
                    cls.curr_lvl.exit_platform.update_label()
                except StopIteration:
                    break


class Colors():
    """Contains used colors"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    FINISH_GREEN = (67, 170, 139)
    BG_COLOR = BLACK
    LVL_BG_COLOR = (50, 50, 50)
    LVL_RECT_COLOR = (17, 167, 122)
    LVL_RECT_HOVER_COLOR = (10, 100, 73)
    TEXT_COLOR = WHITE
    DRONE_COLOR = GRAY


class Fonts():
    """Basic fonts"""
    BASE_FONT_SIZE = 20
    TITLE_FONT_SIZE = 4 * BASE_FONT_SIZE
    BASIC_FONT = pygame.font.Font('fonts/montserrat.ttf', BASE_FONT_SIZE)
    BIGGER_FONT = pygame.font.Font('fonts/montserrat.ttf', BASE_FONT_SIZE * 2)
    TITLE_FONT = pygame.font.Font(
        'fonts/montserrat-semibold.ttf', TITLE_FONT_SIZE)
    STAR_FONT_BIG = pygame.font.Font('fonts/star_font.ttf', BASE_FONT_SIZE * 2)
    STAR_FONT = pygame.font.Font('fonts/star_font.ttf', BASE_FONT_SIZE)


class Text(pygame.sprite.Sprite):
    """Creates a sprite containing the text"""

    def __init__(self, font, text, color, mode = "center", text_func = None):
        super().__init__()
        self.font = font
        self.color = color
        self.text = text
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.mode = mode
        self.text_func = text_func

    def update_text(self, text):
        text = str(text)
        if text != self.text:
            self.text = text
            self.image = self.font.render(text, True, self.color)
            n_rect = self.image.get_rect()
            if self.mode == "center": n_rect.center = self.rect.center
            elif self.mode == "topright": n_rect.topright = self.rect.topright
            else: n_rect.topleft = self.rect.topleft
            self.rect = n_rect

    def update(self, *args):
        if self.text_func is not None:
            self.update_text(self.text_func())


def avg(*args):
    return sum(args)/len(args)
