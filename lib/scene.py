import pygame as pg
from threading import Timer
from lib.config import *


class Cooldown:
    def __init__(self, toggle):
        self.timer = Timer(.2, toggle);

    def start_timer(self, toggle):
        self.timer.start()
        toggle()



class Scene:

    def __init__(self, name, sm, em):
        self.em = em
        self.sm = sm
        self.sounds = self.sm.game.sounds
        self.cooldown = False
        

    def toggle_cooldown(self):
        self.cooldown^=True

    def cancel_timer(self):
        self.toggle_cooldown()

    def handle_events(self, cb):
        for event in pg.event.get():
            if event.type == pg.QUIT: pg.quit(); exit(0)
            if event.type == pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    pg.quit()

                    exit(0)

            if cb: cb(event)
