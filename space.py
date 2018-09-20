import pygame as pg
from config import *
import os



class Space:


    def __init__(self, id, pos, type):
        self.id = id # the index of space positions
        self.type = type
        self.layer = 1

        self.color = colors['grey']
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]

        self.filled = False
        self.card = None # the card object filling the space, if there

        self.image = pg.transform.smoothscale(
            pg.image.load(
                os.path.join(img_dir, 'place.png')
            ), (scale_value, scale_value)
        )

        self.rect = [
            (self.x),
            (self.y),
            (size),
            (size)
        ]


    def draw(self):
        gameDisplay.blit(self.image, (self.x,self.y))


    def update(self):
        pass
