from datetime import datetime
import csv



class Player:


    def __init__(self, name,):
        self.name = name
        self.birth = datetime.now().strftime('_%Y-%m-%d_%H%M')
        self.count = 0

        self.file = 'results/' + str(self.name)
        self.w = csv.writer(open(self.file + self.birth + '.csv', "w"))
        self.w.writerow(['Round','Type','Variation',
            'Duration','Moves', 'Order', 'Score'])


    def commit(self, round, type, vari, dur, moves, order):
        output = {
            'round': round,
            'type': type,
            'vari': vari,
            'dur': dur,
            'moves': moves,
            'order': order,
            'score': self.score(order)
        }

        return output


    def score(self, o):
        f = s = 0

        # Calculate score with the "ratio of repetition"
        # proposed by Cofer 1966:
        # RR = ((Correctly sequenced cards)-(Correct sequence fragments))/
        # (total number of cards - 1)
        # at least 2 adjacent cards in correct order constitute a fragment

        # count correctly seqeunced cards  
        for i, n in enumerate(o):
            if n == o[-1]:
                if n == o[i - 1] + 1: s+=1
            elif i == 0:
                if n == o[i + 1] - 1: s+=1
            elif o[i-1] and o[i+1]:
                if n == o[i - 1] + 1 or n == o[i + 1] - 1: s+=1

        # count correct sequence fragments
        for i, n in enumerate(o):
            if o[i] == o[0]:
                pass
            elif i != 5:
                if o[i] == o[i - 1] + 1 and o[i] != o[i + 1] -1:
                    f+=1
            elif i == 5 and o[i] == o[i - 1] + 1:
                f+=1
            else:
                pass

        # calculate RR
        score = float(s - f)/5

        return(score)
