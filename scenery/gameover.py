import pygame as pg
from lib.scene import Scene
from lib.config import *

class S(Scene):


    def start(self, info):
        self.player = self.sm.game.player
        self.background = bgs['green']

        self.gameoverfont = font1
        self.gameoverblurb = self.gameoverfont.render('Game Over. Well Done!', True, (0, 0, 0))
        self.gameoverblurb_rect = self.gameoverblurb.get_rect(center=(display_width/2, display_height/2.5))


    def draw(self):
        gameDisplay.blit(
            self.gameoverblurb,
            self.gameoverblurb_rect
        )


    def update(self):
        self.handle_events(self.events)


    def end(self, state):
        pass


    def events(self, event):
        if event.type==pg.MOUSEBUTTONDOWN:
            self.end('ROUND')
