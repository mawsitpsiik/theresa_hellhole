# SPDX-FileCopyrightText: 2017 John Edgar Park for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Circuit Playground NeoPixel
import time
import board
from rainbowio import colorwheel
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# choose which demos to play
# 1 means play, 0 means don't!
color_chase_demo = 1
flash_demo = 1
rainbow_demo = 0
rainbow_cycle_demo = 0


def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

while True:
    if color_chase_demo:
        color_chase(RED, 0.1)
        color_chase(GREEN, 0.1)
        color_chase(RED, 0.1)
        color_chase(GREEN, 0.1)
        color_chase(RED, 0.1)
        color_chase(CYAN, 0.1)
        color_chase(OFF, 0.1)


