import pygame
from level import *
from constants import Colors

# TEST LVL
test = Level()

# BLOCKS
test.new_block(935, 0, 50, 650)
test.new_block(400, 650, 1300, 50)

test.new_spawner(300, 300, 100, 30, (255, 0, 0))
test.new_spawner(600, 200, 150, 30, (255, 255, 0))
test.new_spawner(700, 500, 90, 40, (255, 0, 255))

# LVL 2
test2 = Level()
