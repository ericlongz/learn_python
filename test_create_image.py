#!/usr/bin/python3

#import PIL as pillow
from PIL import Image

img = Image.new('RGB', (60,30), color = 'red')
img.save('pil_red.png')
