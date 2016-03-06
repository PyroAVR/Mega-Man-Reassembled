
import pygame
from pygame.locals import *


#call this class in main
class Megaman(pygame.sprite.Sprite):

###VARIABLES SHARED BY ALL INSTANCES###

#image path
path = "insert path here"
#Example path = "/Mega-Man-Reassembled/assets/mmdance.gif"

#make the sprite image
image = pygame.image.load(path)

#if it's a .gif
image = image.convert_alpha()

#set start position
startpos = (320,240) #start in the middle of the screen


    #initialize the sprite
    def __init__(self, startpos):

        #not necessary for megaman because only one instance.....probably
        pygame.sprite.Sprite.__init__(self, self.groups) #add to groups

        #variables for each individual instance
        self.image = Megaman.image
        self.pos = startpos
        self.rect = self.image.get_rect()


    #update the sprite
    def update(self, seconds)

        #add where sprite is drawn according the key presses, mouse movments, etc...

        #for example:
        seld.rect.center = pygame.mouse.get_pos()
