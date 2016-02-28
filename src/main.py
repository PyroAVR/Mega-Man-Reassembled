#!/usr/bin/env python3
#This is just to get us started, before we get structure worked out.
import sge

#This implementation detail frustrates programmers from low-level languages...
from Game import Game
from Menu import Menu

Game()
background = sge.gfx.Background([], sge.gfx.Color("white"))



sge.game.start_room = Menu(background = background)

if __name__ == '__main__':
    sge.game.start()
