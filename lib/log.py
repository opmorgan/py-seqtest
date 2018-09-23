import pygame as pg
from lib.config import *
# the log will have a row that that records the results of every round: (1) round number; (2) Condition (e.g., control_A_1; verbal_B_2); (3) order of cards when subject pressed "done"; (4) number of moves); (4) score

# # Scoring was based on entirely correct sequences and correct
# fragments. Calculation was performed using the ‘Ratio of
# repetition’ (RR) proposed by Cofer (1966). Thus, two cartoonlike
# drawings in correct succession were considered the shortest
# fragment of a sequence to be evaluated. Each correct fragment was
# computed independently of its right or wrong position in the
# whole sequence (for instance, if the correct answer was 1 2 3 4 5 6
# and the subject’s answer was: 2 3 4 6 1 5, the sequence 2 3 4
# represented a correct fragment). The RR was obtained using the
# following formula:
# RR ¼
# ðCorrectly sequenced cardsÞ  ðCorrect sequence fragmentsÞ
# Total number of cards  1
# Thus, RR values run from zero to one. The task was administered
# without a time limit.

# to get time:
# import timer
# datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

Log = [
    {'subject': 'Subject_057'},
    {'date' '2013-11-19 09:38'}
    {'output':
        {'round_num': 1,
        'type': 'control',
        'variation': 'A',
        'round_dur' : 13.468,
        'num_moves': 17,
        'order': [1 2 3 4 6 5],
        'score': .95.,
        }
    }
]

class Log:

    def __init__(self, round_num, round_cond, moves, order, score):
        self.round_num = ['N/A'] * len(rounds);
        self.round_cond = ['N/A'] * len(rounds);
        self.moves = ['N/A'] * len(rounds);
        self.order = ['N/A'] * len(rounds);
        self.score = ['N/A'] * len(rounds);

        def place(self, space):
            self.sounds["place"].play()
            space.card = self
            self.space = space
            self.inhand = False
            self.update_pos(space.pos)

        def update_log(self):
            self.pos = pos
            self.x = self.pos[0]
            self.y = self.pos[1]

        def write_log(self)
