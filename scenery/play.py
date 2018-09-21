import pygame as pg
from datetime import datetime
from event import Event
from scene import Scene
from card import Card
from space import Space
from config import *
import csv



class S(Scene):


    def start(self, info):
        self.sm.game.state = "ROUND"
        self.start_time = datetime.now()
        self.moves = 0
        self.font = font1

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
                'Press any key when done.', 
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
                self.order.append(space.card.id+1)

        self.sm.game.state = state

        row = []
        for key, val in self.commit(self.sm.game.player).items():
            print(key, val)
            row.append(val)
        self.sm.game.player.w.writerow(row)
        
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

        if event.type==pg.MOUSEBUTTONDOWN:
            for card in self.cards:
                if card.inhand == False:
                    if utils.mouse_chk(pg.mouse.get_pos(), card, size):
                         card.pick_up(self)
                         self.em.push(card)
                else:
                    for space in self.spaces:
                        if utils.mouse_chk(pg.mouse.get_pos(), space, size):
                            card.place(space)
                            self.moves += 1

        if event.type==pg.KEYDOWN:
            i = 0
            for card in self.cards:
                if card.space and card.space.type == 'target': i+=1
                else: i=0
                
            if i == 6: # MAKES ADVANCING POSSIBLE ONLY WHEN 6 CARDS HAVE BEEN PLACES
                if self.sm.round == len(rounds):
                    print('indeed, this is the last round!')
                    self.end('GAMEOVER')

                else:
                    self.end('FINISHED')
