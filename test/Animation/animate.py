#!/usr/bin/python

import sys
import time
import pygame


#set width and height variables
global width, height
width = 640
height = 480

#loading images

def load(imgpath):
    img = pygame.image.load(imgpath)
    return img


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.images = []
        self.images.append(load('megaman1.png'))
        self.images.append(load('megaman2.png'))
        self.images.append(load('megaman3.png'))
        self.images.append(load('megaman4.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 300, 300) #images are 300 x 300 pixels

    def update(self):

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():

    pygame.init()
    screen = pygame.display.set_mode((width, height))

    sprite = Player()
    group = pygame.sprite.Group(sprite)

    while True:

            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            group.update()
            group.draw(screen)
            pygame.display.flip()

            time.sleep(0.1)


if __name__ == '__main__':
    main()
