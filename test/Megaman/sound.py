import pygame
#import winsound
#import sys

#pygame.mixer.init()

path = 'lib\laser.wav'


def pew():

    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    #s = Sound() ##use snack sound player##
    #s.read(path)
    #s.play()

    #pygame.mixer.init()
    #sound = pygame.mixer.Sound('path')
    #sound.play(0)


if __name__ == '__main__':
    while True:
        pew()
