# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This demo will fill the screen with white, draw a black box on top
and then print Hello World! in the center of the display

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Display:
    def __init__(
        self,
        WIDTH: int = 128,
        HEIGHT: int = 32
    ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.oled_reset = digitalio.DigitalInOut(board.D4)

        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, self.i2c, addr=0x3C, reset=self.oled_reset)

        self.bitmap = [[0] * WIDTH for i in range(HEIGHT)]


    def clear_bitmap(
        self,
    ):
        self.bitmap = [[0] * self.WIDTH for i in range(self.HEIGHT)]

    def set_bitmap(
        self,
        x: int = 0,
        y: int = 0,
        v: int = 0
    ):
        self.bitmap[x][y] = v

    def draw_bitmap(
        self
    ):
        image = Image.new("1", (self.WIDTH, self.HEIGHT))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.WIDTH, self.HEIGHT), outline=0, fill=0)
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.bitmap[i][j] == 0: continue
                draw.rectangle((j, i, j, i), outline=255, fill=255)
        self.oled.image(image)

    def clear(
        self
    ):
        self.oled.fill(0)
    
    def update(
        self
    ):
        self.oled.show()
