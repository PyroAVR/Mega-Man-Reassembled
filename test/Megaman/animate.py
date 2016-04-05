#!/usr/bin/python

import sys
import time
import pygame
import sound


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

        self.healthModifier = 0 #change for powerups and items
        self.health = 10 + self.healthModifier

        self.speed = 20

        self.isJump = False
        self.gravity = 1
        self.yvel = 0

        self.x = xpos
        self.y = ypos

        self.right_images = []
        self.right_images.append(load('lib/megaman1.png'))
        self.right_images.append(load('lib/megaman2.png'))
        self.right_images.append(load('lib/megaman3.png'))
        self.right_images.append(load('lib/megaman4.png'))

        self.index = 0
        self.image = self.right_images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 60, 60) #images are 60 x 60 pixels ##fix this later for collision## ###needs to move with the sprite###


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


    def jump(self, velocity):

        self.yvel = -velocity
        self.isJump = True


    def animate_blast(self, direction):

        rightBlast = load('lib/megaman_blast_right.png')
        leftBlast = load('lib/megaman_blast_left.png')


        if direction == 'right':
            self.image = rightBlast

        if direction == 'left':
            self.image = leftBlast
        else:
            print 'you screwed up'


    def update_jump(self):

        self.yvel += self.gravity
        self.y += self.yvel

        if self.y > 510:
            #self.y = 500
            self.isJump = False
            self.yvel = 0


    def fall(self):

        if self.y < 500 and self.isJump == False:
            self.jump(-25)


    def update(self):
        #put jump and run physics here
        return


    def check_collision(self, object):

        self.rect = pygame.Rect(self.x, self.y, 120, 120)
        objectPoint = (object.x, object.y)

        if self.rect.collidepoint(objectPoint) == True:
            print "collision!"
            self.health -= object.damage

        else:
            #print "nope"
            #nothing collided
            return


    def render(self):

        screen.blit(self.image, (self.x, self.y))



class Blaster(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos, direction):

        self.image = load('lib/blast.png')

        self.speed = 5

        self.x = xpos
        self.y = ypos


        if direction == 'right':
            self.moveRight()
        elif direction == 'left':
            self.moveLeft()
        else:
            print "you forgot a contructor idiot"


    def moveRight(self):

        self.x = self.x + self.speed


    def moveLeft(self):

        #for i in range (0, 20):
            #self.x = self.x - self.speed
            #self.render()
            #time.sleep(.1)

        self.x = self.x - self.speed


    def render(self):

        screen.blit(self.image, (self.x, self.y))




class Enemy(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos, health, damage):

        self.x = xpos
        self.y = ypos

        self.health = health
        self.damage = damage


    def render(image):

        screen.blit(image, (self.x, self.y))



#class Juan(Enemy):

class Baddy(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos):

        #super((Enemy, self), __init__())

        self.x = xpos
        self.y = ypos

        self.health = 10
        self.damage = 10

        self.image = load('lib/megaman1.png')

        self.rect = pygame.Rect(self.x, self.y, 60, 60)



    def render(self):

        screen.blit(self.image, (self.x, self.y))




def main():

    pygame.init()

    global screen
    screen = pygame.display.set_mode((width, height))

    sprite = Player(100,500)

    bkgd = pygame.image.load('lib/bkgd.jpg')

    enemy = Baddy(400, 200)

    #counter = 0

    blast_list = [] #make a global in own class later
    isBlasting = False



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
                   sprite.jump(12)
                   #sprite.y -= 20
                   #sprite.isJump = True

               #if ourevent.key == pygame.K_DOWN:
                   #sprite.animate_jump()
                   #sprite.jump(-12)
                   #sprite.y += 20
                   #sprite.isJump = True

               if ourevent.key == pygame.K_d:

                   #blaster1 = Blaster(sprite.x + 20, sprite.y + 20, 'right')
                   sound.pew()
                   blast_list.append(Blaster(sprite.x + 20, sprite.y + 20, 'right'))
                   isBlasting = True
                   #sprite.animate_blast("right")

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
            if sprite.x <= width -  60:
                if leftPressed == False: #and sprite.isJump == False:
                    rightPressed = True
                    sprite.isJump = False
                    sprite.animate_right()
                    sprite.x = sprite.x + sprite.speed
                    time.sleep(.04) #sleep is adding delay to blaster

        if keys[pygame.K_LEFT]:
            if rightPressed == False: #and sprite.isJump == False:
                if sprite.x >= 0:
                    leftPressed = True
                    sprite.isJump = False
                    sprite.animate_standing()
                    sprite.x = sprite.x - sprite.speed
                    time.sleep(.04) #sleep is adding delay to blaster


        #if leftPressed == False and rightPressed == False: #and sprite.isJump == False:
            #sprite.animate_standing()


        sprite.update()
        sprite.render()

        sprite.fall()

        enemy.render()

        #if isBlasting == True and sprite.isJump == False:

        #if isBlasting == True:

        for blaster in blast_list:
            blaster.moveRight()
            blaster.render()

            if blaster.x > 1000:
                blast_list.remove(blaster)

            #else:
                #isBlasting = False
                #blastCount = 0


        if sprite.isJump == False and rightPressed == False and leftPressed == False:
            sprite.animate_standing()


        if sprite.isJump == True:
            sprite.update_jump()


        sprite.check_collision(enemy)

        if sprite.health <= 0:
            sys.exit()

        pygame.display.flip()


        #time.sleep(0.1)



if __name__ == '__main__':
    main()
