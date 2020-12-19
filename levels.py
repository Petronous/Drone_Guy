import pygame
from level import *
from constants import Colors

# TEST LVL
test = Level(size=(1382, 778))

# BLOCKS
test.new_block(935, 0, 50, 650)  # 1
test.new_block(400, 650, 1300, 50)  # 2
# SPAWNERS
test.new_spawner(300, 300, 100, 30, (255, 0, 0))  # 1
test.new_spawner(600, 200, 150, 30, (255, 255, 0))  # 2
test.new_spawner(700, 500, 90, 40, (255, 0, 255))  # 3


# LVL 2
lvl2 = Level(size=(1382, 778), score_to_win=10, time_remaining=120)
# SPAWNERS
lvl2.new_spawner(600, 300, 100, 30, (0, 0, 255))  # 1
lvl2.new_spawner(800, 300, 100, 30, (0, 255, 0))  # 2
lvl2.new_spawner(100, 700, 100, 30, (255, 255, 0))  # 3
lvl2.new_spawner(1282, 700, 100, 30, (255, 0, 0))  # 4
# BLOCKS
lvl2.new_block(500, 250, 50, 150)  # 1
lvl2.new_block(900, 250, 50, 150)  # 2
lvl2.new_block(700, 0, 50, 650)  # 3
lvl2.new_block(500, 400, 450, 50)  # 4
lvl2.new_block(0, 550, 300, 50)  # 5
lvl2.new_block(1082, 550, 300, 50)  # 6
lvl2.new_block(500, 628, 50, 150)  # 7
lvl2.new_block(900, 628, 50, 150)  # 8


# LVL 3
lvl3 = Level(size=(1382, 778), time_remaining=180, score_to_win=8)
# SPAWNERS
lvl3.new_spawner(150, 678, 100, 30, (255, 0, 0))  # 1
lvl3.new_spawner(541, 678, 100, 30, (0, 255, 0))  # 2
lvl3.new_spawner(882, 678, 100, 30, (0, 0, 255))  # 3
lvl3.new_spawner(1232, 678, 100, 30, (255, 255, 0))  # 4
# BLOCKS
lvl3.new_block(0, 350, 250, 50)  # 1
lvl3.new_block(200, 600, 200, 50)  # 2
lvl3.new_block(250, 200, 150, 50)  # 3
lvl3.new_block(400, 200, 50, 578)  # 4
lvl3.new_block(450, 575, 125, 50)  # 5
lvl3.new_block(575, 225, 282, 100)  # 6
lvl3.new_block(691, 0, 50, 100)  # 7
lvl3.new_block(691, 500, 50, 278)  # 8
lvl3.new_block(857, 575, 150, 50)  # 9
lvl3.new_block(982, 200, 50, 578)  # 10
lvl3.new_block(1032, 200, 150, 50)  # 11
lvl3.new_block(1179, 350, 250, 50)  # 12
lvl3.new_block(1032, 600, 200, 50)  # 13
