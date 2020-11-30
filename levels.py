import pygame
from level import *

# LVL
test = Level()

# BLOCKS
test.blocks.append(Block(935, 0, 50, 650, test.group, graphics.Colors.))
test.blocks.append(Block(400, 650, 1300, 50, test.group))



lvl_list = []
lvl_list.append(test)
