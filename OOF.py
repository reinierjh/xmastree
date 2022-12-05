from tree import RGBXmasTree
from colorzero import Color
import random
from time import sleep
from datetime import datetime, time

def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else:
        return start <= now or now < end

tree = RGBXmasTree()
colors = [Color('red'), Color('green')] # add more if you like
tree.brightness = 0.1
tree_peak = (1.0, 0.84, 0.0)

try:
    while True:
        day_night = "night" if in_between(datetime.now().time(), time(23), time(7)) else "day"
        if day_night == "night":
            tree.off()
            continue
            sleep(60)
        if day_night == "day":
            tree[3].color = tree_peak
            pixel = random.choice(tree)
            if pixel.value == tree_peak:
                continue
            for color in colors:
                pixel.color = color
except KeyboardInterrupt:
    tree.close()
