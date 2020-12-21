import pygame
from level import *
from constants import Colors, Fonts

# TEST LVL
test = Level('Tutorial', size=(1382, 778), star_points = [1, 2, 3], time_remaining=60)
# HELPTEXTS
test.new_label(10, 50, Fonts.BASIC_FONT, "WASD or Arrows to move", Colors.TEXT_COLOR)
test.new_label(10, 85, Fonts.BASIC_FONT, "Load crates by landing on colored platforms", Colors.TEXT_COLOR)
test.new_label(10, 120, Fonts.BASIC_FONT, "Drop crates by landing on platforms of their color", Colors.TEXT_COLOR)
test.new_label(10, 155, Fonts.BASIC_FONT, "Transport as many crates as possible", Colors.TEXT_COLOR)
test.new_label(10, 190, Fonts.BASIC_FONT, "Land on green platform with stars to finish level", Colors.TEXT_COLOR)
test.new_label(10, 220, Fonts.BASIC_FONT, "if you don't want to wait for the timer to do so", Colors.TEXT_COLOR)
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
lvl2 = Level('Tunnel', size=(1382, 778), star_points = [10, 17, 24], time_remaining=180)  # could reach max 22
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
lvl2.new_block(100, 550, 200, 50)  # 5
lvl2.new_block(1082, 550, 300, 50)  # 6
lvl2.new_block(500, 628, 50, 150)  # 7
lvl2.new_block(900, 628, 50, 150)  # 8

# PLATFORMS
lvl2.make_exit_platform(0, 550, 100, 50)  # Exit platform


# LVL 3
lvl3 = Level('Columns', size=(1382, 778), time_remaining=180, star_points = [8, 13, 19])  # could reach max 18
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
