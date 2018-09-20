import pygame as pg
from config import *



class Card:


    def __init__(self, id, pos, sounds, type, variation):
        self.id = id or 0
        self.layer = 2

        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]

        self.type = type
        self.variation = variation

        self.image = pg.transform.smoothscale(
            pg.image.load(
                os.path.join(img_dir, str(self.type + '_' + self.variation + '_' + str(self.id+1) + '.png'))
            ), (scale_value, scale_value)
        )
        self.size = self.image.get_rect().width
        self.rect = pg.Rect(self.image.get_rect())

        self.sounds = sounds

        self.space = None # Whatever space the card belonds to.
        self.inhand = False

    def draw(self):
        gameDisplay.blit(self.image,(self.x, self.y))


    def update(self):
        if self.inhand == True:
            pos = [
                pg.mouse.get_pos()[0] - (size // 2),
                pg.mouse.get_pos()[1] - (size //2)
            ]
            self.update_pos(pos)


    def place(self, space):
        self.sounds["place"].play()
        space.card = self
        self.space = space
        self.inhand = False
        self.update_pos(space.pos)


    def pick_up(self, scene):
        self.sounds["pick up"].play()
        self.space = None
        self.inhand = True


    def update_pos(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
