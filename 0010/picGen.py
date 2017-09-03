#! /usr/bin/env python3
# -*- conding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def randkey(len=4):
    keys = 'abcdefghijklmnopqrstuvwxyz0123456789'
    result =  ''
    while len(result) < len:
        result = result + random.choice(keys)
    return result
def randchr():
    return chr(random.randint(65, 90))

def randColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def createPic():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 40)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randColor())
    for t in range(4):
        draw.text((60 * t + 10, 10), randchr(), font=font, fill=randColor2())
    image = image.filter(ImageFilter.BLUR)
    return image
if __name__ == '__main__':
    img = createPic()
    img.show()