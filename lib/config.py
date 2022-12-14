import pygame as pg
import lib.utils as utils
import tkinter as tk
import os
import sys

# SYS VARS

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


# get screen size. 
root = tk.Tk()

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

display_size = (display_width,display_height)
margin = { 'y': display_height * .1, 'x': display_height * 0 }
# set size of cards
scale_value = int((display_width - (margin['x'] * 2)) // 6)

# set font
# fontSize = display_height//24 # for regular fonts
fontSize = display_height//32 # for mono fonts
font1_path = resource_path(os.path.join("resources", "fonts", "SourceCodePro-Regular.ttf"))
pg.font.init()
font1 = pg.font.Font(font1_path, fontSize)

img_dir = resource_path(os.path.join('resources', 'images'))
sound_dir = resource_path(os.path.join('resources', 'sounds'))


colors = {
    'grey' : (0, 0, 0, 0.3),
}

sounds = {
    "deal": {
        'loc': os.path.join(sound_dir, 'shuffle.wav'),
        'vol': 0.4
    },
    "pick up": {
        'loc': os.path.join(sound_dir, 'pickup.wav'),
        'vol': 0.4
    },
    "place": {
        'loc': os.path.join(sound_dir, 'place.wav'),
        'vol': 0.6
    },
    "swap": {
        'loc': os.path.join(sound_dir, 'swap.wav'),
        'vol': 0.6
    },
    "done": {
        'loc': os.path.join(sound_dir, 'done.wav'),
        'vol': 0.4
    }
}

time_limit = 240.0

class Round:

    def __init__(self, num, type, variation):
        self.num = num
        self.type = type
        self.variation = variation

rounds =  [
    Round(1, 'control', 'A'),
    Round(2, 'verbal', 'A'),
    Round(3, 'verbal', 'B'),
    Round(4, 'verbal', 'C'),
    Round(5, 'spatial', 'A'),
    Round(6, 'spatial', 'B'),
    Round(7, 'spatial', 'C'),
    Round(8, 'cartoon', 'A'),
    Round(9, 'cartoon', 'B'),
    Round(10, 'cartoon', 'C'),
]

bgs = {
    'green': utils.scaler(os.path.join(img_dir, 'bg.png'), display_size)
}

gameDisplay = pg.display.set_mode(display_size, pg.FULLSCREEN) # makes window

clock = pg.time.Clock() # game clocks

size = utils.scaler(os.path.join(img_dir, 'place.png'), (scale_value, scale_value)).get_width()

def make_blurb(font, name, text, sub, mod2):
    v = font.render(text, True, (0, 0, 0))
    m = 0 if sub else v.get_width()
    v_rect = v.get_rect(center=((display_width-m)/2, display_height/mod2))

    return { name: { 'blurb': v, 'rect': v_rect } }


# CONFIG VARS
# these may not be used
ESCAPE_SEQUENCE = pg.K_1 and pg.K_0
