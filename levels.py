import pygame
from level import *
from constants import Colors

# LVL
test = Level()

# BLOCKS
test.blocks.append(Block(935, 0, 50, 650, test.group, Colors.GREEN))
test.blocks.append(Block(400, 650, 1300, 50, test.group, Colors.GREEN))



lvl_list = []
lvl_list.append(test)
