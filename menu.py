import pygame
pygame.init()

# CONSTANTS – TEMP
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

TEXT_COLOR = GRAY
BG_COLOR = WHITE

BASIC_FONT_SIZE = 20
BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
TITLE_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE*4)


def show_menu(game_state):
    game_state.DISPLAY_SURFACE.fill(BG_COLOR)

    text_surf = TITLE_FONT.render("Level select", True, TEXT_COLOR)
    text_rect = text_surf.get_rect()

    game_state.DISPLAY_SURFACE.blit(text_surf, text_rect)
