import pygame as pg
from lib.scene import Scene
from lib.config import *

class S(Scene):


    def start(self, info):
        self.player = self.sm.game.player
        self.background = bgs['green']
        self.font = font1

        self.blurbs = {
            **make_blurb(self.font, 'over','Game Over. Well Done!', True, 2.5),
            **make_blurb(self.font, 'end','Press ESCAPE to quit.', True, 2)
        }


    def draw(self):
        for k in self.blurbs:
            gameDisplay.blit(self.blurbs[k]['blurb'], self.blurbs[k]['rect'])



    def update(self):
        self.handle_events(self.events)


    def end(self, state):
        pass


    def events(self, event):
        if event.type==pg.MOUSEBUTTONDOWN:
            self.end('ROUND')
