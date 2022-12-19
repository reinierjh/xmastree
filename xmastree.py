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
def on_message(client, userdata, message):
    global message_received
    global tree_status
    time.sleep(1)
    message_received=str(message.payload.decode("utf-8"))
    decoded_message
    

tree = RGBXmasTree()
colors = [Color('red'), Color('green'), Color('blue')] # add more if you like
tree.brightness = 0.05
tree_peak = (1, 32, 255)

try:
    while True:
        day_night = "night" if in_between(datetime.now().time(), time(23), time(7)) else "day"
        if day_night == "night":
            tree.off()
            sleep(60)
            continue
        if day_night == "day":
            tree[3].color = tree_peak
            pixel = random.choice(tree)
            if pixel.value == tree_peak:
                continue
            pixel.color = random.choice(colors)
#            sleep(1)
except KeyboardInterrupt:
    tree.close()
