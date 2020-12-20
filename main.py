import pygame
import sys

import graphics
import level
import levels
import drone
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
    Game_state.WIN_W = round(DISP_INFO.current_w * 0.9)
    Game_state.WIN_H = round(DISP_INFO.current_h * 0.9)
    print(Game_state.WIN_W, Game_state.WIN_H)

    # INIT
    Game_state.DISP_SURF = pygame.display.set_mode(
        (Game_state.WIN_W, Game_state.WIN_H))
    Game_state.drone = drone.Drone()

    add_missing_levels()
    load_level_stats()

    # CAPTION
    pygame.display.set_caption("Drone guy")


    # CREATING A CLASS MENU INSTANCE
    Game_state.MENU = graphics.Menu(width=Game_state.WIN_W, height=Game_state.WIN_H)
    Game_state.MENU.make_rects()

    # GAME LOOP
    while True:
        # CHECKING FOR QUIT
        check_for_quit()

        handle_key_press()

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


def handle_key_press():
    """Handles input from user depending on Game_state.room"""
    if Game_state.room == "menu":
        menu_handle_input()

    if Game_state.room == "lvl":
        lvl_handle_input()

    if Game_state.room == "game_over":
        game_over_handle_input()


def menu_handle_input():
    """Return the index of the lvl the user has chosen by clicking on it's rect (=> 0 = LVL 1), if nothing was chosen returns None"""
    graphics.draw_menu()
    # RETURN VALUE IS LVL NUMBER CHOSEN - 1 OR NONE IF NO LVL WAS CHOSEN
    choice = None
    for button in Game_state.MENU.lvl_buttons:
        if button.is_over(pygame.mouse.get_pos()):
            for event in pygame.event.get(pygame.MOUSEBUTTONUP):
                choice = Game_state.MENU.lvl_buttons.index(button)

    # RUN CHOSEN LVL
    if choice is not None:
        Game_state.room = "lvl"
        Game_state.curr_lvl = Game_state.lvl_list[choice]

        Game_state.curr_lvl.setup()

        Game_state.drone = drone.Drone()
        Game_state.drone.pos_x, Game_state.drone.pos_y = Game_state.curr_lvl.drone_start_pos
        Game_state.score = 0


def lvl_handle_input():
    Game_state.curr_lvl.time_remaining -= Game_state.FPS_CLOCK.get_time() / 1000

    # GAME OVER
    if Game_state.curr_lvl.time_remaining <= 0 or Game_state.drone.health <= 0:
        Game_state.room = "game_over"
        save_level_stats()
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


def game_over_handle_input():
    for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                Game_state.room = "menu"
                load_level_stats()
                return

    graphics.draw_game_over()


def save_level_stats():
    lines = []
    with open("data.txt", 'r') as fr:
        lvl = Game_state.curr_lvl
        lvl_ix = None
        for a, line in enumerate(fr):
            s = line.split()
            if s[0] == str(lvl.name):
                lvl_ix = a
                line = f"{lvl.name} {max(Game_state.score, int(s[1]))} {max(len(lvl.exit_platform.text), int(s[2]))}\n"
            lines.append(line)
        assert lvl_ix is not None, "LEVEL SAVE NOT FOUND"

    if len(lines) > 0:
        with open("data.txt", 'w') as fw:
            fw.write("".join(lines))


def load_level_stats():
    with open("data.txt", 'r') as fr:
        for line in fr:
            s = line.split()
            Game_state.lvl_stats[s[0]] = (int(s[1]), int(s[2]))


def add_missing_levels():
    lvl_names = [str(i.name) for i in Game_state.lvl_list]
    lines = []
    try:
        fr = open("data.txt", 'r')
        for line in fr:
            s = line.split()
            lvl_names.remove(s[0])
            lines.append(line)
    except:
        pass
    fw = open("data.txt", 'w')
    for i in lvl_names:
        lines.append(f"{i} 0 0\n")
    fw.write("".join(lines))
    fw.close()


if __name__ == "__main__":
    main()
