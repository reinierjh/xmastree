from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

try:
    for pixel in tree:
        pixel.color = (1, 235, 100)
except KeyboardInterrupt:
    tree.close()
