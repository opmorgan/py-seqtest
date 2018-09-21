import pygame as pg
from config import *



class Scene:


    def __init__(self, name, sm, em):
        self.em = em
        self.sm = sm
        self.sounds = self.sm.game.sounds


    def handle_events(self, cb):
        for event in pg.event.get():
            if event.type == pg.QUIT: pg.quit(); exit(0)
            if event.type == pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    pg.quit()

                    if (hasattr(self, "timer")):
                        self.timer.cancel()

                    exit(0)
            if cb: cb(event)
