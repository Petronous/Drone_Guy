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
lvl2 = Level(size=(1382, 778))

# SPAWNERS
# 1
lvl2.new_spawner(600, 300, 100, 30, (0, 0, 255))

# 2
lvl2.new_spawner(800, 300, 100, 30, (0, 255, 0))

# 3
lvl2.new_spawner(100, 700, 100, 30, (255, 255, 0))

# 4
lvl2.new_spawner(1282, 700, 100, 30, (255, 0, 0))


# BLOCKS
# 1
lvl2.new_block(500, 250, 50, 150)

# 2
lvl2.new_block(900, 250, 50, 150)

# 3
lvl2.new_block(700, 0, 50, 650)

# 4
lvl2.new_block(500, 400, 450, 50)

# 5
lvl2.new_block(0, 550, 300, 50)

# 6
lvl2.new_block(1082, 550, 300, 50)

# 7
lvl2.new_block(500, 628, 50, 150)

# 8
lvl2.new_block(900, 628, 50, 150)


# LVL 3
lvl3 = Level(size=(1382, 778))

# SPAWNERS
# 1
lvl3.new_spawner(150, 678, 100, 30, (255, 0, 0))

# 2
lvl3.new_spawner(541, 678, 100, 30, (0, 255, 0))

# 3
lvl3.new_spawner(882, 678, 100, 30, (0, 0, 255))

# 4
lvl3.new_spawner(1232, 678, 100, 30, (255, 255, 0))


# BLOCKS
# 1
lvl3.new_block(0, 350, 250, 50)

# 2
lvl3.new_block(200, 600, 200, 50)

# 3
lvl3.new_block(250, 200, 150, 50)

# 4
lvl3.new_block(400, 200, 50, 578)

# 5
lvl3.new_block(450, 575, 125, 50)

# 6
lvl3.new_block(575, 225, 282, 100)

# 7
lvl3.new_block(691, 0, 50, 100)

# 8
lvl3.new_block(691, 500, 50, 278)

# 9
lvl3.new_block(857, 575, 150, 50)

# 10
lvl3.new_block(982, 200, 50, 578)

# 11
lvl3.new_block(1032, 200, 150, 50)

# 12
lvl3.new_block(1179, 350, 250, 50)

# 13
lvl3.new_block(1032, 600, 200, 50)
