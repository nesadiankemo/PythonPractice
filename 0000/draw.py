#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PIL import Image, ImageDraw, ImageFont

# draw text in picture
def draw_text(img, text):
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('arial.ttf', 30)
	size = draw.textsize(text, font)
	x = img.size[0] - size[0]
	y = 0
	draw.text((x, y), text, font=font, fill=(255, 0, 0))

if __name__ == '__main__':
	img = Image.open(sys.argv[1])
	try:
		text = sys.argv[2]
	except Exception as e:
		text = '13'
	draw_text(img, text)
	img.show()