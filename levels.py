import pygame
from level import *
from constants import Colors, Fonts

# TEST LVL
test = Level('Tutorial', size=(1382, 778), star_points = [1, 2, 3], time_remaining=60, drone_start_pos = (410, 600))
# BLOCKS
# test.new_block(935, 0, 50, 650)  # 1
# test.new_block(400, 650, 1300, 50)  # 2
# SPAWNERS
test.new_spawner(150, 500, 150, 30, (255, 0, 0))  # 1
test.new_spawner(900, 700, 150, 30, (0, 255, 0))  # 2
test.new_spawner(1200, 300, 150, 30, (0, 0, 255))  # 3
# PLATFORMS
test.make_exit_platform(400, 650, 100, 50)  # Exit platform
# TEXT
test.new_text("Welcome to Drone Guy!", (350, 100), font=Fonts.BIGGER_FONT)
test.new_text("Try moving your drone by using the ARROW KEYS or WASD", (350, 140))
test.new_text("Your objective is to transport crates from these colorful", (350, 170))
test.new_text("platforms to a platform of the same color as the crate", (350, 200))

test.new_text("Be wary of the HEALTH of your drone,", (1000, 140))
test.new_text("the TIME you have left and the SCORE you", (1000, 170))
test.new_text("need to achieve to complete the level", (1000, 200))

test.new_text("Press SPACE to exit the level and get back to the level selection", (700, 320))
# test.new_text("an exit platform will show up, you might not want to use", (700, 350))
# test.new_text("it right away, as it unlocks after you get enough score to pass", (700, 380))
# test.new_text("the level, but you can go for a higher rating if you continue", (700, 410))



# LVL 2
lvl2 = Level('Baskets', size=(1382, 778), star_points = [15, 27, 35], time_remaining=180, drone_start_pos = (10, 500))
# SPAWNERS
lvl2.new_spawner(671, 300, 100, 30, (0, 0, 255))  # 1
lvl2.new_spawner(671, 700, 100, 30, (0, 255, 0))  # 2
lvl2.new_spawner(100, 700, 100, 30, (255, 255, 0))  # 3
lvl2.new_spawner(1282, 700, 100, 30, (255, 0, 0))  # 4
lvl2.new_spawner(100, 300, 100, 30, (255, 0, 255)) # 5
lvl2.new_spawner(1282, 300, 100, 30, (0, 255, 255)) # 5

# BLOCKS
lvl2.new_block(500-34, 250, 50, 150)  # 1
lvl2.new_block(900-34, 250, 50, 150)  # 2
lvl2.new_block(700-34, 0, 50, 250)  # 3
lvl2.new_block(500-34, 400, 450, 50)  # 4
lvl2.new_block(100, 550, 200, 50)  # 5
lvl2.new_block(1082, 550, 300, 50)  # 6
lvl2.new_block(500-34, 628, 50, 150)  # 7
lvl2.new_block(900-34, 628, 50, 150)  # 8
lvl2.new_block(700-34, 400, 50, 200)  # 9
lvl2.new_block(0, 400, 300, 50)  # 10
lvl2.new_block(1082, 400, 300, 50)  #12
lvl2.new_block(250, 250, 50, 150)  # 13
lvl2.new_block(1082, 250, 50, 150)  # 14

# PLATFORMS
lvl2.make_exit_platform(0, 550, 100, 50)  # Exit platform


# LVL 3
lvl3 = Level('Columns', size=(1382, 778), time_remaining=180, star_points = [8, 13, 19], drone_start_pos = (676, 450))  # could reach max 18
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
lvl3.new_block(691, 550, 50, 278)  # 8
lvl3.new_block(857, 575, 150, 50)  # 9
lvl3.new_block(982, 200, 50, 578)  # 10
lvl3.new_block(1032, 200, 150, 50)  # 11
lvl3.new_block(1179, 350, 250, 50)  # 12
lvl3.new_block(1032, 600, 200, 50)  # 13

# PLATFORMS
lvl3.make_exit_platform(691, 500, 50, 50) # Exit platform

# LVL 4
lvl4 = Level(name="Slalom", time_remaining=180, star_points=[5, 9, 13], size=(1382, 778), drone_start_pos=(1282, 275))

# SPAWNERS
lvl4.new_spawner(25, 100, 100, 30, (255, 0, 0)) # 1
lvl4.new_spawner(25, 708, 100, 30, (0, 255, 0)) # 2
lvl4.new_spawner(1312, 100, 100, 30, (0, 0, 255)) # 3
lvl4.new_spawner(1312, 708, 100, 30, (255, 255, 0)) # 4

# BLOCKS
lvl4.new_block(200, 0, 50, 80) # 1
lvl4.new_block(400, 90, 50, 80) # 2
lvl4.new_block(1000, 0, 50, 80) # 3
lvl4.new_block(1000, 170, 150, 50) # 4
lvl4.new_block(1000, 490, 150, 50)  # 5
lvl4.new_block(1000, 540, 50, 130) # 6
lvl4.new_block(400, 648, 50, 130) # 7
lvl4.new_block(200, 540, 50, 130) # 8
lvl4.new_block(0, 170, 1000, 370) # 9
lvl4.new_block(600, 0, 50, 80)  # 10
lvl4.new_block(800, 90, 50, 80)  # 11
lvl4.new_block(600, 540, 50, 130)  # 12
lvl4.new_block(800, 648, 50, 130)  # 13

# EXIT PLATFORM
lvl4.make_exit_platform(1182, 325, 200, 50)
