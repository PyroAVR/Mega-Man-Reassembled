#!/usr/bin/env python3
#This is just to get us started, before we get structure worked out.
import sge
import xsge_gui
#This implementation detail frustrates programmers from low-level languages...
from Game import Game
from Menu import Menu

#defaults
game_width	=  1280
game_height	=  720

Game(width= game_width, height= game_height)

xsge_gui.init()



sge.game.start_room = Menu()

if __name__ == '__main__':
    sge.game.start()
