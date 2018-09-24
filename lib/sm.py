from lib.config import *
import os
import sys
from threading import Timer


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

class SM:


    def __init__(self, game, em):
        self.game = game
        self.current_scene = None # Intro, Game, round finished, Game over
        self.scenes = []
        self.next_scene = None
        self.previous_scene = None

        self.round = 0

        for name in self.game.scenes:
            for f in os.listdir(resource_path('scenery')):
                base = os.path.splitext(f)[0]
                if base == name:
                    SCENE = __import__('scenery.'+ base, fromlist=['S'])
                    self.scenes.append(SCENE.S(name, self, em))


    def start_scene(self, info):
        if self.current_scene == None:
            self.current_scene = self.scenes[0]
            self.update_scenes()
            self.current_scene.start()

        else:
            self.update_scenes()
            self.current_scene.em.entities = []
            self.current_scene.start(info)


    def end_scene(self):
        # def commit(round, type, vari, dur, moves, order):
        pass

    def timer(self, func):
        timer = Timer(10, func(), ())
        time.start()


    def draw(self):
        gameDisplay.blit(self.current_scene.background, (0,0))
        self.current_scene.draw()


    def update(self):
        self.current_scene.update()


    def add_scene(self, scene):
        self.scenes.append(scene)


    def update_scenes(self):
        scenes = self.scenes
        current = self.current_scene
        if len(scenes) > 0:
            for i, s in enumerate(scenes):
                if current == s:
                    if not len(scenes) <= i + 1:
                        self.next_scene = scenes[i + 1]
                        self.previous_scene = scenes[i - 1]


    def change_scene(self):
        if self.game.state == 'ROUND':
            self.current_scene = self.previous_scene
            self.start_scene(rounds[self.round])
        elif self.game.state == 'GAMEOVER':
            self.current_scene = self.scenes[-1]
            self.start_scene(rounds[self.round])
        else:
            self.current_scene = self.next_scene
            self.start_scene(rounds[self.round])
