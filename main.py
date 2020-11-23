import graphics
import level
import drone
import menu

import pygame
import sys


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
    WIN_W = 800
    WIN_H = 600

    # INIT
    DISP_SURF = pygame.display.set_mode((WIN_W, WIN_H))

    # CAPTION
    pygame.display.set_caption("Drone guy")

    # GAME LOOP
    while True:
        check_for_quit()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def check_for_quit():
    """Checks if the user pressed either the X or ESCAPE if so calls terminate()"""
    if pygame.event.get(pygame.QUIT):
        terminate()

    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            terminate()
        pygame.event.post(event)


def terminate():
    """Exits the program"""
    pygame.quit()
    sys.exit()


def key_pressed():
    """Return True if any key is pressed"""
    return any(pygame.event.get(pygame.KEYDOWN))


def handle_key_press():
    pass


if __name__ == "__main__":
    main()
