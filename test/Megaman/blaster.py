import pygame


#loading images
def load(imgpath):
    img = pygame.image.load(imgpath)
    return img



#some variables
blast_list = [] #make a globals in own class later
isBlasting = False



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

        self.x = self.x - self.speed


    def render(self):

        screen.blit(self.image, (self.x, self.y))
