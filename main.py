import graphics
import level
import drone
import menu

import pygame
import sys


class Game_state():
    """Most of the info any other file would need to use from main.py"""

    def __init__(self, room=None, drone=None, obstacles=[], spawners=[], DISPLAY_SURFACE=None, lvl_list=[], lvl_rects=[]):
        self.room = room
        self.drone = drone
        self.obstacles = obstacles
        self.spawners = spawners
        self.DISPLAY_SURFACE = DISPLAY_SURFACE
        self.lvl_list = lvl_list
        self.lvl_rects = lvl_rects


def main():
    """Main function of the game, contains the game loop and initial setup"""
    # PYGAME INIT
    pygame.init()

    # CONSTANTS
    # FPS
    FPS_CLOCK = pygame.time.Clock()
    FPS = 30

    # DISPLAY SURFACE
    # WIDTH AND HEIGHT
    DISP_INFO = pygame.display.Info()
    WIN_W = round(DISP_INFO.current_w * 0.9)
    WIN_H = round(DISP_INFO.current_h * 0.9)

    # INIT
    DISP_SURF = pygame.display.set_mode(
        (WIN_W, WIN_H), pygame.RESIZABLE)

    # CAPTION
    pygame.display.set_caption("Drone guy")

    # CREATION OF GAME_STATE INSTANCE
    state = Game_state("menu", drone.Drone(), None, None, DISP_SURF)

    # GAME LOOP
    while True:
        # CHECKING FOR QUIT
        check_for_quit()

        handle_key_press(state)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def terminate():
    """Exits the program"""
    pygame.quit()
    sys.exit()


def check_for_quit():
    """Checks if the user has exited the program"""
    if pygame.event.get(pygame.QUIT):
        terminate()

    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            terminate()
        pygame.event.post(event)


def key_pressed():
    """Returns True if any key is pressed"""
    return any(pygame.event.get(pygame.KEYDOWN))


def handle_key_press(game_state):
    """Handles input from user depending on game_state.room"""
    if game_state.room == "menu":
        graphics.draw_menu(game_state)
        # RETURN VALUE IS LVL NUMBER CHOSEN - 1 OR NONE IF NO LVL WAS CHOSEN
        choice = menu.handle_input(game_state)
        # RUN CHOSEN LVL – TODO


if __name__ == "__main__":
    main()
