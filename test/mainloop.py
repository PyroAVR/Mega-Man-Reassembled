#!/usr/bin/python

import sys
import os
import time
import pygame
from pygame import *
import MegaMan

#.get_rect(scrub)

def main():

    #add time updates later to run at certain fps/ups

    #set up pygame window
    pygame.init()
    pygame.mouse.set_visible(1)
    window = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Mega-Man Reassembled")

    #fill the background
    background = pygame.Surface(window.get_size())
    background = background.convert()
    background.fill((250,250,250))

    #blit background to the screen
    window.blit(background,(0,0))
    pygame.display.flip()

    #make sprite groups
    allgroup = pygame.sprite.Group()
    meggroup = pygame.sprite.Group()
    Megaman.groups = allgroup, meggroup #add megaman to both groups

    #add the sprites
    megman = Megaman()

    #times for updating
    FPS = 50
    UPS = 50
    seconds = 1 #currentely for testing, replace with UPS later


    #game loop
    while True:

        #quit when exit
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        #update() #use this later

        #update the sprites
        allsprites.clear(window, backgroud)
        allsprites.update(seconds)
        allsprites.draw(window)
        pygame.display.flip()

        #blit to the screen, again
        window.blit(background, (0,0))
        pygame.display.flip()


#start it
if __name__ == '__main__' : main()


def update():

    #put updates here

    #blit to the screen, again
    screen.blit(background, (0,0))
    pygame.display.flip()
