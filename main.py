import pygame
import sys

import graphics
import level
import levels
import drone
import menu
from constants import Game_state


def main():
    """Main function of the game, contains the game loop and initial setup"""
    # CONSTANTS
    # FPS
    Game_state.FPS_CLOCK = pygame.time.Clock()
    FPS = 30

    # DISPLAY SURFACE
    # WIDTH AND HEIGHT
    DISP_INFO = pygame.display.Info()
    WIN_W = round(DISP_INFO.current_w * 0.9)
    WIN_H = round(DISP_INFO.current_h * 0.9)
    print(WIN_W, WIN_H)

    # INIT
    Game_state.DISP_SURF = pygame.display.set_mode(
        (WIN_W, WIN_H))
    Game_state.drone = drone.Drone()

    # CAPTION
    pygame.display.set_caption("Drone guy")

    # GAME LOOP
    while True:
        # CHECKING FOR QUIT
        check_for_quit()

        handle_key_press()

        handle_resize()

        pygame.display.update()
        Game_state.FPS_CLOCK.tick(FPS)


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


def handle_resize():
    """ Doesn't work at all """
    # for event in pygame.event.get(pygame.VIDEORESIZE):
    #     print("VIDEORESIZE")
    #     DISP_INFO = pygame.display.Info()
    #     WIN_W = DISP_INFO.current_w
    #     WIN_H = DISP_INFO.current_h
    #     Game_state.DISP_SURF = pygame.display.set_mode((WIN_W, WIN_H), pygame.RESIZABLE)
    #     print(WIN_H, WIN_W)
    pass


def handle_key_press():
    """Handles input from user depending on Game_state.room"""
    if Game_state.room == "menu":
        graphics.draw_menu()
        # RETURN VALUE IS LVL NUMBER CHOSEN - 1 OR NONE IF NO LVL WAS CHOSEN
        choice = menu.handle_input()
        # RUN CHOSEN LVL
        if choice is not None:
            Game_state.room = "lvl"
            Game_state.curr_lvl = Game_state.lvl_list[choice]
            Game_state.curr_lvl.time_remaining = Game_state.curr_lvl.init_time
            Game_state.drone = drone.Drone()
            Game_state.drone.pos_x, Game_state.drone.pos_y = Game_state.curr_lvl.drone_start_pos
            Game_state.score = 0

    if Game_state.room == "lvl":
        Game_state.curr_lvl.time_remaining -= Game_state.FPS_CLOCK.get_time() / 1000
        if Game_state.curr_lvl.time_remaining <= 0 or Game_state.drone.health <= 0:
            Game_state.room = "game_over"
            return
        # HANDLE EVENTS
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    Game_state.drone.control_v = -1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    Game_state.drone.control_v = 1
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    Game_state.drone.control_h = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    Game_state.drone.control_h = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    Game_state.drone.control_v = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    Game_state.drone.control_v = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    Game_state.drone.control_h = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    Game_state.drone.control_h = 0

            else:
                pygame.event.post(event)

        Game_state.drone.update()
        graphics.draw_level(Game_state, Game_state.curr_lvl, Game_state.drone)

    if Game_state.room == "game_over":
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                Game_state.room = "menu"
                return

        graphics.draw_game_over()


if __name__ == "__main__":
    main()
