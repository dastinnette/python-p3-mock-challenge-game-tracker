#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    g1 = Game("Monopoly")
    g2 = Game("Chess")
    p1 = Player("Adam")
    p2 = Player("Emiley")    
    r1 = Result(p1, g1, 2500)
    r1 = Result(p1, g1, 3500)
    r2 = Result(p1, g2, 15)

    ipdb.set_trace()
