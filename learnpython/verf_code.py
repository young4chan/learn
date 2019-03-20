#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# random alphabet
def rndChar():
    return chr(random.randint(65, 90))

# random color 1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# random color 2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
Image = Image.new('RGB', (width, height), (255, 255, 255))
# new Font object
font = ImageFont.truetype('Arial.tiff', 36)
# draw object
draw = ImageDraw.Draw(image)
# fill pixel
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# output text
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# blur
image = image.filter(ImageFilter.BLUR)
iamge.save('code.jpg', 'jpeg')
