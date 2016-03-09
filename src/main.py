#!/usr/bin/env python3
#This is just to get us started, before we get structure worked out.
import sge
#This implementation detail frustrates programmers from low-level languages...
from Game import Game
from Menu import Menu
from DialogBox import DialogBox

#defaults
game_width	=  1280
game_height	=  720

Game(width= game_width, height= game_height)
font = sge.gfx.Font("assets/Fonts/PressStart2P.ttf",size=24)
b = DialogBox(font=font, text="hello world", char_sprite=None)
b.render()
objects = [b]
#Move this to the menu class
background = sge.gfx.Background([], sge.gfx.Color("white"))



sge.game.start_room = Menu(background=background, objects=objects)

if __name__ == '__main__':
    sge.game.start()
