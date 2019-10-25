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

def makeShip():
    created = 0
    while created == 0:
        name = str(input('Enter name: '))
        if len(name) > 0 and len(name) < 100:
            created = 1
        elif len(name) == 0:
            print('Name cannot be empty.')
        elif len(name) >= 100:
            print('Name too long (max. 100 characters).')
        else:
            print('Name not valid.')
        # Add confirmation?
    return(Ship(name))

def statusReport():
    try:  
        ship #check ship exists
    except NameError:
        print('Ship not found.')
    else:
        print('\n' + ship.sname + ship.name + ' | ' + ship.sclass + ' class \n')
        if ship.alert == 1:
            print('\t' + '\033[1;30;43m YELLOW ALERT ' + '\x1b[0m')
        elif ship.alert > 1:
            print('\t' + '\033[1;37;41m RED ALERT ' + '\x1b[0m') # round values down
        print('\t' + 'hull integrity:' + '\t' + 'OK      (' + str(ship.hull_integrity*100) + '%)')
        # option for hull breach
        if ship.warp_core_status == 0:
            print('\t' + 'warp core:' + '\t' + 'offline (' + str(ship.warp_core_charge*100) + '%)')
        else:
            print('\t' + 'warp core:' + '\t' + 'ONLINE  (' + str(ship.warp_core_charge*100) + '%)')
        if ship.shields_status == 0:
            print('\t' + 'shields:'  + '\t' + 'offline (' + str(ship.shields_integrity*100) + '%)')
        else:
            print('\t' + 'shields:'  + '\t' + 'ONLINE  (' + str(ship.shields_integrity*100) + '%)')
        if ship.phaser_status == 0:
            print('\t' + 'phaser banks:' + '\t' + 'offline')
        else:
            print('\t' + 'phaser banks:' + '\t' + 'ONLINE')
        print('\t' + 'photon torpedoes: ' + str(ship.photon_torpedoes))
        print('\t' + 'crew complement: ' + str(ship.crew))
    return
    
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
