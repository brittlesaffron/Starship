# -*- coding: utf-8 -*-
import numpy as np

#OBJECTIVE: find and rescue the ship

class Ship:     
    sname = 'U.S.S. '
    symbol = '=o'   # class variable shared by all instances
    sclass = 'Intrepid'
    def __init__(self, name):  # instance variables unique to each instance
        self.name = name # add U.S.S.
        self.warp_core_status = 1 # Online
        self.warp_core_charge = 1 # between 0 and 1 (100%) #phasers drain it
        self.shields_status = 0 # Offline # Drains warp core while online
        self.shields_integrity = 1 # between 0 and 1 (100%)
        self.phaser_status = 0 # Offline # Drains warp core while online
        self.hull_breach = 0 # Unused for now
        self.hull_integrity = 1 # between 0 and 1 (100%)
        self.alert = 0 # 0=no, 1=yellow, 2=red
        self.crew = 150
        self.photon_torpedoes = 38 # Full complement
        
map_height = 10
map_length = 10
starchart = [['*'] * map_height] * map_length
    
def makeStarchart(height, width):
    #set max (20?) and min (2?) values
    starchart = [[0]*width for x in range(height)]
    return starchart

def updateStarchart(starchart, x, y, value): #do we need this
    #if value == "ship" -> 1, etc... ?
    starchart[y][x] = value
    return starchart

def printStarchart(height, length): #pass starchart as argument
    #"translate"from number to symbol
    for i in range(height):
        print((('*' + '\t') * length) + '\n') #change '*' for coordinates
        # test = [[list(range(10))] for x in range(10)]
        # starchart[0][0][0]
    #add ship status
        
while True:
    print('[N]ew Game', '\t', '[L]oad Saved Game', '\t', '[Q]uit', '\n')
    choice = str(input('> ')).lower()
    if choice == 'n':
        ship = makeShip() # TODO
        statusReport() # TODO
    if choice == 'l':
        break #add way to load from save
    if choice == 'q':
        break
    # printStarchart(10, 10)
    break
