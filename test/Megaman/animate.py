#!/usr/bin/python

import sys
import time
import pygame


#set width and height variables
global width, height
width = 1000
height = 640

#loading images

def load(imgpath):
    img = pygame.image.load(imgpath)
    return img


class Player(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos):

        self.speed = 20

        self.isJump = False

        self.x = xpos
        self.y = ypos

        self.right_images = []
        self.right_images.append(load('lib/megaman1.png'))
        self.right_images.append(load('lib/megaman2.png'))
        self.right_images.append(load('lib/megaman3.png'))
        self.right_images.append(load('lib/megaman4.png'))

        self.index = 0
        self.image = self.right_images[self.index]
        self.rect = pygame.Rect(5, 5, 60, 60) #images are 60 x 60 pixels


    def set_position(self, xpos, ypos):

		self.x = xpos
		self.y = ypos


    def animate_right(self):

        #update running image
        self.index += 1
        if self.index >= len(self.right_images):
            self.index = 0
        self.image = self.right_images[self.index]


    def animate_standing(self):

        self.image = self.right_images[0]


    def animate_jump(self):

        self.image = load('lib/megaman_jump.png')
        #self.isJump = True


    def update(self):
        #put jump and run physics here
        return


    def render(self):

        screen.blit(self.image, (self.x, self.y))



class Blaster(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos, direction):

        self.image = load('lib/blast.png')

        self.speed = 10

        self.x = xpos
        self.y = ypos

        if direction == 'right':
            self.moveRight()
        elif direction == 'left':
            self.moveLeft()
        else:
            print "you forgot a contructor idiot"


    def moveRight(self):

        #for i in range (0, 20):
            #self.x = self.x =+ self.speed
            #print "moving right"
            #self.render()
            #time.sleep(1)

            #if i > 20:
                #return

        self.x = self.x + self.speed
        #self.render()


    def moveLeft(self):

        for i in range (0, 20):
            self.x = self.x - self.speed
            self.render()
            time.sleep(.1)


    def render(self):

        screen.blit(self.image, (self.x, self.y))



def main():

    pygame.init()

    global screen
    screen = pygame.display.set_mode((width, height))

    sprite = Player(100,500)

    bkgd = pygame.image.load('lib/bkgd.jpg')

    #counter = 0

    #blaster stuff
    #blastNumber = 0

    isBlasting = False
    blastCount = 0
    blast_list = []


    while True:


        #counter += 1
        #print counter

        #if counter == 10:
            #sprite.isJump == False
            #counter = 0


        screen.blit(bkgd, (0,0))


        for ourevent in pygame.event.get():
           if ourevent.type == pygame.QUIT:
               pygame.quit()
               sys.exit(0)

           if ourevent.type == pygame.KEYDOWN:
               if ourevent.key == pygame.K_UP:
                   sprite.animate_jump()
                   sprite.y -= 20
                   sprite.isJump = True

               if ourevent.key == pygame.K_DOWN:
                   sprite.animate_jump()
                   sprite.y += 20
                   sprite.isJump = True

               if ourevent.key == pygame.K_d:

                   #blaster1 = Blaster(sprite.x + 20, sprite.y + 20, 'right')

                   blast_list.append(Blaster(sprite.x + 20, sprite.y + 20, 'right'))
                   isBlasting = True

                   #if blastNumber == 0:
                    #   print 'ay'
                     #  blaster1 = Blaster(sprite.x + 20, sprite.y + 20, 'right') #add or subtract to sprite location later for starting point of blaster
                      # blastNumber = blastNumber + 1

                  #elif blastNumber == 1:
                    #   blaster2 = Blaster(sprite.x + 20, sprite.y + 20, 'right')
                     #  blastNumber = blastNumber + 1

                   #elif blastNumber == 2:
                    #   blaster3 = Blaster(sprite.x + 20, sprite.y + 20, 'right')
                     #  blastNumber = blastNumber + 1

                   #elif blastNumber == 3:
                    #   blaster4 = Blaster(sprite.x + 20, sprite.y + 20, 'right')
                     #  blastNumber = blastNumber + 1



        leftPressed = False
        rightPressed = False


        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_RIGHT]:
            if leftPressed == False: #and sprite.isJump == False:
                rightPressed = True
                sprite.isJump = False
                sprite.animate_right()
                sprite.x = sprite.x + sprite.speed
                time.sleep(.04)

        if keys[pygame.K_LEFT]:
            if rightPressed == False: #and sprite.isJump == False:
                leftPressed = True
                sprite.isJump = False
                sprite.animate_standing()
                sprite.x = sprite.x - sprite.speed
                time.sleep(.04)


        #if leftPressed == False and rightPressed == False: #and sprite.isJump == False:
            #sprite.animate_standing()


        sprite.update()
        sprite.render()


        if isBlasting == True and sprite.isJump == False:

            if blastCount < 200:

                blastCount = blastCount + 1

                for blaster in blast_list:
                    blaster.moveRight()
                    blaster.render()

                #blaster1.moveRight()
                #blaster1.render()

                #if blastNumber == 0:
                #    blastCount = blastCount + 1
                #    blaster1.moveRight()
                #    blaster1.render()

                    #if blastNumber == 1:
                    #    blaster2.moveRight()
                    #    blaster2.render()

                    #    if blastNumber == 2:
                    #        blaster3.moveRight()
                    #        blaster3.render()

                    #        if blastNumber == 3:
                    #            blaster4.moveRight()
                    #            blaster4.render()

            else:
                isBlasting = False
                blastCount = 0



        #print blastNumber

        pygame.display.flip()


        #time.sleep(0.1)



if __name__ == '__main__':
    main()
