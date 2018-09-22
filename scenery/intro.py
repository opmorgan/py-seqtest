from scene import Scene
from player import Player
from config import *
import pygame as pg
import pygame_textinput as pg_textinput


class S(Scene):

    def start(self):
        self.sm.game.state = "INTRO"
        self.game = self.sm.game
        self.background = bgs['green']
        self.font = font1
        self.blurbs = {
            **make_blurb(self.font, 'welcome','Welcome to the sequence game! Enter ID and then "Return" to begin.', True, 2.5),
            **make_blurb(self.font, 'prompt','Subject ID: ', False, 2)
        }

        self.textinput = pg_textinput.TextInput("",font1_path, fontSize, True)
        self.textinput_pos = self.textinput.surface.get_rect(center=(display_width/2, display_height/2))
        self.textinput.surface.get_rect()
        self.textinput.keyrepeat_intial_interval_ms = 2500
        self.textinput.keyrepeat_interval_ms = 2500 # 5000 works one key at a time at 10000


    def draw(self):
        for k in self.blurbs:
            gameDisplay.blit(self.blurbs[k]['blurb'], self.blurbs[k]['rect'])

        gameDisplay.blit(
            self.textinput.surface,
            [self.blurbs['prompt']['rect'][0] + self.blurbs['prompt']['blurb'].get_width(),
            self.blurbs['prompt']['rect'][1]]
        )


    def update(self):
        self.handle_events(self.events)


    def events(self, event):
        if self.textinput.update(event):
            self.sm.game.player_create(self.textinput.get_text())
        
            self.sm.change_scene()
