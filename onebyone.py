from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

colors = [Color('red'), Color('green')] # add more if you like

tree.brightness = 0.1

try:
    while True:
        for color in colors:
            for pixel in tree:
                pixel.color = color
except KeyboardInterrupt:
    tree.close()
