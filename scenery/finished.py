from event import Event
from scene import Scene
import time  
import pygame as pg
from config import *



class S(Scene):

    def start(self, info):
        self.sounds["done"].play()
        self.start_time = time.time()

        self.background = bgs['green']
        self.welcomefont = font1
        self.welcomeblurb = self.welcomefont.render('Round Over! Well done. Click to continue.', True, (0, 0, 0))
        self.welcomeblurb_rect = self.welcomeblurb.get_rect(center=(display_width/2, display_height/2.5))


    def draw(self):
        gameDisplay.blit(self.welcomeblurb, self.welcomeblurb_rect)


    def update(self):
        self.handle_events(self.events)


    def end(self, state):
        # add 1 to sm's round counter if it's not the last round
        if not self.sm.round == len(rounds) - 1:
            self.sm.round += 1
            self.sm.game.state = state

        self.sm.change_scene()


    def events(self, event):
        if ((time.time() - self.start_time) > 0.5):
            if event.type==pg.MOUSEBUTTONDOWN:

                self.end('ROUND')

                #timer.start_timer(self.toggle_cooldown)
