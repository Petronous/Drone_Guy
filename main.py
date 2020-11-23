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
    DISP_INFO = pygame.display.Info()
    WIN_W = DISP_INFO.current_w - 100
    WIN_H = DISP_INFO.current_h - 100

    # INIT
    DISP_SURF = pygame.display.set_mode(
        (WIN_W, WIN_H), pygame.RESIZABLE)

    # CAPTION
    pygame.display.set_caption("Drone guy")

    # GAME LOOP
    while True:
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.type == pygame.QUIT:
                terminate()
            if event.key == pygame.K_ESCAPE:
                terminate()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


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
