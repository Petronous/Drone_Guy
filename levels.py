import pygame
from level import *
from constants import Colors

# LVL
test = Level()

# BLOCKS
test.blocks.append(Block(935, 0, 50, 650, test.group))
test.blocks.append(Block(400, 650, 1300, 50, test.group))

test.spawners.append(Spawner(300, 300, 100, 30, (255, 0, 0), test.group))
test.spawners.append(Spawner(600, 200, 150, 30, (255, 255, 0), test.group))
test.spawners.append(Spawner(1000, 500, 90, 40, (255, 0, 255), test.group))

lvl_list = []
lvl_list.append(test)
