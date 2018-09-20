from random import shuffle
import pygame as pg
from config import *



def shuffler (r):


    shuff = [i for i in range(r)]
    shuffleagain = 1

    while shuffleagain: 
        # re-shuffle until no two sequential cards are neighbors
        shuffle(shuff)
        idx = 0
        for j in range(r - 1):
            if shuff[j] - shuff[j+1] == 1 or shuff[j] - shuff[j+1] == -1:
                shuffleagain = 1
            else:
                idx += 1
            if idx == 5:
                shuffleagain = 0
                return shuff


def scaler (file, factor):
    file = pg.image.load(file)
    return pg.transform.scale(file, factor)


def mouse_chk (mp, pos, size):
    return (mp[0]>=pos.x) and mp[0]<=(pos.x + size) and mp[1]<=(pos.y + size) and mp[1]>=(pos.y)
