import pygame


#image loading
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
