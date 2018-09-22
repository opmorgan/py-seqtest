import pygame as pg
from threading import Timer
import time
from datetime import datetime
from event import Event
from scene import Scene
from card import Card
from space import Space
from config import *
import csv


class S(Scene):

    def timeover(self):
        print("Timed out.")
        self.end("FINISHED")


    def start(self, info):
        self.sm.game.state = "ROUND"
        self.start_time = datetime.now()
        self.moves = 0
        self.font = font1
        self.t0 = 2
        #self.timer = Timer(time_limit, self.timeover)
        #self.timer.start()

        self.order = []

        self.background = bgs['green']
        self.type = info.type
        self.variation = info.variation

        self.sounds["deal"].play()
        self.shuff = utils.shuffler(6)

        for i in range(6):
            x = size * i + margin['x']
            s = size * self.shuff[i] + margin['x']

            self.em.add(
                Space(i, [x, display_height - size - margin['y']], 
                    'pool'),
                Space(i, [x, margin['y']], 'target'),
                Card(i,  [s, display_height - size - margin['y']],
                    self.sounds, self.type, self.variation),
            )

        self.cards = [e for e in self.em.entities if isinstance(e,Card)]
        self.spaces = [e for e in self.em.entities if isinstance(e,Space)]


        self.blurbs = {
            **make_blurb(self.font, 'inst1',
                'Click to pick up and place'
                ' the cards in a logical order above.',
                True, 2.2),
            **make_blurb(self.font, 'inst2',
                'Press ENTER when done.', 
                True, 1.8)
        }



    def draw(self):
        for k in self.blurbs:
            gameDisplay.blit(self.blurbs[k]['blurb'], 
                    self.blurbs[k]['rect'])
        for e in self.em.entities:
            e.draw()


    def update(self):
        for e in self.em.entities:
            e.update()

        self.handle_events(self.events)



    def end(self, state):
        for space in self.spaces:
            if space.type == 'target':
                if (hasattr(space.card, "id")):
                    self.order.append(space.card.id+1)
                else:
                    self.order.append(None)

        if (self.sm.round == (rounds[-1].num - 1)):
            self.sm.game.state = "GAMEOVER"
        else:
            self.sm.game.state = state

        row = []
        for key, val in self.commit(self.sm.game.player).items():
            row.append(val)
        self.sm.game.player.w.writerow(row)

        # self.timer.cancel()

        self.sm.change_scene()

    def commit(self, player):
        return player.commit(
            self.sm.round,
            self.type,
            self.variation,
            str(datetime.now() - self.start_time),
            self.moves,
            self.order
        )

    def events(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if time.time() - self.t0 > .2:
                for card in self.cards:
                    if card.inhand == False:
                        if utils.mouse_chk(pg.mouse.get_pos(), card, size):
                             card.pick_up(self)

                             space = next((s for s in self.spaces if (s.card == card)), None)
                             if (hasattr(space, "card")):
                                 space.card = None

                             self.em.push(card)
                    else:
                        for space in self.spaces:
                            if utils.mouse_chk(pg.mouse.get_pos(), space, size):
                                card.place(space)
                                self.moves += 1

                self.t0 = time.time()


        if event.type==pg.KEYDOWN:
            if time.time() - self.t0 > .2 :
                if event.unicode == ">":
                    self.end('FINISHED')
                    self.t0 = time.time()
                elif event.key == pg.K_RETURN:
                    i = 0
                    for card in self.cards:
                        if card.space and card.space.type == 'target': i+=1
                        else: i=0 

                    if i == 6:
                        self.end('FINISHED')

                    self.t0 = time.time()
