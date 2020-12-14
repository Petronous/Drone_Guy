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
lvl2 = Level(size = (1382, 778))

# Spawner 1
lvl2.new_spawner(600, 300, 100, 30, (0, 0, 255))

# Spawner 2
lvl2.new_spawner(800, 300, 100, 30, (0, 255, 0))

# Spawner 3
lvl2.new_spawner(100, 700, 100, 30, (255, 255, 0))

# Spawner 4
lvl2.new_spawner(1282, 700, 100, 30, (255, 0, 0))


# Block 1
lvl2.new_block(500, 250, 50, 150)

# Block 2
lvl2.new_block(900, 250, 50, 150)

# Block 3
lvl2.new_block(700, 0, 50, 650)

# Block 4
lvl2.new_block(500, 400, 450, 50)

# Block 5
lvl2.new_block(0, 550, 300, 50)

# Block 6
lvl2.new_block(1082, 550, 300, 50)

# Block 7
lvl2.new_block(500, 628, 50, 150)

# Block 8
lvl2.new_block(900, 628, 50, 150)
