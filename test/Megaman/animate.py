#!/usr/bin/python

import sys
import time
import pygame


#set width and height variables
global width, height
width = 1080
height = 640

#loading images

def load(imgpath):
    img = pygame.image.load(imgpath)
    return img


class Player(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos):

        self.speed = 20

        self.isjump = False

        self.x = xpos
        self.y = ypos

        self.images = []
        self.images.append(load('lib/megaman1.png'))
        self.images.append(load('lib/megaman2.png'))
        self.images.append(load('lib/megaman3.png'))
        self.images.append(load('lib/megaman4.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 300, 300) #images are 300 x 300 pixels


    def set_position(self, xpos, ypos):

		self.x = xpos
		self.y = ypos


    def animate_right(self):

        #update running image
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


    def animate_standing(self):

        self.image = self.images[0]


    def animate_jump(self):

        self.image = load('lib/megaman_jump.png')


    def update(self):
        #put jump and run physics here
        return


    def render(self):

        screen.blit(self.image, (self.x, self.y))



def main():

    pygame.init()

    global screen
    screen = pygame.display.set_mode((width, height))

    sprite = Player(100,500)

    bkgd = pygame.image.load('lib/bkgd.jpg')


    while True:

        screen.blit(bkgd, (0,0))


        for ourevent in pygame.event.get():
           if ourevent.type == pygame.QUIT:
               pygame.quit()
               sys.quit(0)
           if ourevent.type == pygame.KEYDOWN:
               if ourevent.key == pygame.K_UP:
                   sprite.animate_jump()
                   sprite.y -= 20
               #if ourevent.key == pygame.K_LEFT and sprite.x > 10:
                   #sprite.x -= 5


        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_RIGHT]:
            sprite.animate_right()
            sprite.x = sprite.x + sprite.speed
            time.sleep(.05)
        #else:
            #sprite.animate_standing()
        if keys[pygame.K_LEFT]:
            sprite.x = sprite.x - sprite.speed
            time.sleep(.05)
        #if keys[pygame.K_UP]:      #Use pressed key instead
            #sprite.isjump = True


        sprite.update()
        sprite.render()
        pygame.display.flip()

        #time.sleep(0.1)


if __name__ == '__main__':
    main()
