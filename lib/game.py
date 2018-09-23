from lib.sm import SM
from lib.em import EM
from lib.player import Player
from lib.config import *



class Game:


    def __init__(self, pg, scenes):
        pg.init()
        pg.mixer.init()

        self.scenes = scenes

        self.state = None

        self.sounds = {}
        for k, v in sounds.items():
            self.sounds[k] = pg.mixer.Sound(v['loc'])
            self.sounds[k].set_volume(v['vol'])

        self.pg = pg
        self.started = True
        self.sm = SM(self, EM())
        # for scene in scenes:
        #    self.sm.add_scene(scene)


    def player_create(self, name):
        self.player = Player(name)


    def start(self):
        self.sm.start_scene(None)


    def draw(self):
        self.sm.draw()


    def update(self):
        clock.tick(60)
        self.sm.update()
        self.pg.display.flip()


    def change_state(self, state):
        self.state = state


    def end(self, pg):
        pg.quit()
        quit()
