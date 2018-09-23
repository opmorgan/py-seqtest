#! /usr/local/bin/python3

import pygame as pg
from lib.game import Game
# from lib.config import *


scenes = ["intro", "play", "finished", "gameover"]

g = Game(pg, scenes)

g.start()

while g.started:

    g.draw()
    g.update()
