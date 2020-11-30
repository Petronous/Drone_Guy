import pygame
import sys

import graphics
import level
import levels
import drone
import menu
from game_state import Game_state


def main():
    """Main function of the game, contains the game loop and initial setup"""
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
    Game_state.DISP_SURF = pygame.display.set_mode(
        (WIN_W, WIN_H), pygame.RESIZABLE)

    # CAPTION
    pygame.display.set_caption("Drone guy")

    # GAME LOOP
    while True:
        # CHECKING FOR QUIT
        check_for_quit()

        handle_key_press()

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def terminate():
    """Exits the program"""
    pygame.quit()
    sys.exit()


def check_for_quit():
    """Checks if the user has tried to exit the program"""
    if pygame.event.get(pygame.QUIT):
        terminate()

    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            terminate()
        pygame.event.post(event)


def handle_key_press():
    """Handles input from user depending on Game_state.room"""
    if Game_state.room == "menu":
        graphics.draw_menu()
        # RETURN VALUE IS LVL NUMBER CHOSEN - 1 OR NONE IF NO LVL WAS CHOSEN
        choice = menu.handle_input()
        # RUN CHOSEN LVL – TODO
        if choice is not None:
            Game_state.room = "lvl"
            Game_state.curr_lvl = Game_state.lvl_list[choice]
            graphics.draw_level(Game_state, Game_state.curr_lvl, drone.Drone())

    if Game_state.room == "lvl":
        # Game_state.curr_lvl.update()
        pass


if __name__ == "__main__":
    main()
