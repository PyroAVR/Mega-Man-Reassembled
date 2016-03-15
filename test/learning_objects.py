import sge
#import xsge_tmx
import os

class Game(sge.dsp.Game):
    def __init__(self, height=720, width=1280):
        super().__init__(width=width, height=height)
        self.pause_sprite = sge.gfx.Sprite(name='pause', directory="assets/pausemenu", height=1080, width=1920)
        sge.game.mouse.visible = True;
    def event_key_press(self, key, char):
        if key == 'escape':
            self.event_close()
        elif key == 'f11':
            self.fullscreen = not self.fullscreen
        elif key == 'f8':
            sge.gfx.Sprite.from_screenshot().save("screenshot.png")
        elif key == 'p':
            freezeframe = sge.gfx.Sprite.from_screenshot()
            freezeframe.draw_sprite(self.pause_sprite, 0, 0, 0, 0)
            self.pause(freezeframe)

    def event_close(self):
        self.end()

    def event_paused_key_press(self, key, char):
        if key == 'escape':
            self.event_close()
        else:
            self.unpause()
    def event_paused_close(self):
        self.event_close()


class TestObject(sge.dsp.Object):
    def __init__(self):
        x = 32
        y = 32
        sprite = sge.gfx.Sprite(name="eddieclassic", directory="assets/", width=32, height=32)
        super().__init__(x, y, sprite=sprite)
#    def event_step(self, time_passed, delta_mult):
#        print("Hello World!")

class CustomRoom(sge.dsp.Room):
    def __init__(self, objects, intromusic, intromovie, music, background):
        print("placeholder")
        self.music = None
        self.intromusic = intromusic
        self.sounds = dict()
        super().__init__(objects=objects, background=background)
        self.start()

    #We abstract the room start to it's own method so that it can restart itself.
    def start(self):
        print("placeholder")
        self.intromusic.play()
    def event_step(self, time_passed, delta_mult):
        print("placeholder")



class Generator:
    def __init__(self, filename):
        import json     #this screams bad practice to me
        self.raw_data = ''
        #Python 3 apparently needs a max list size :/  What the heck, guys
        self.objects = [1000]
        with open(filename, 'r') as file:   #with is one of Python's saving graces
            self.raw_data = file.read()
        self.json_data = json.loads(self.raw_data)
        print(self.json_data)
        #How many elements in the top-level array?
        self.json_num_elements = len(self.json_data)
        print(self.json_num_elements)

    def createObjects(self):
        i = 0
        for obj in self.json_data:
            #Do not read the last element.  That is the room descriptor.
            if i == self.json_num_elements -1:
                return
            #so sad the one-liner had to go...
            #how big is the path name?
            sizeof_path = len(obj["sprite"])
            sp_string = obj["sprite"]
            #Where's the last '/' in the sprite field?
            delim = sp_string.rfind("/") +1
            sprite_path = sp_string[0:delim]
            sprite_name = sp_string[delim:sizeof_path]
            print(sprite_path)
            print(sprite_name)
            print(obj["x"])
            s = sge.gfx.Sprite(name=sprite_name, directory=sprite_path, width=obj["width"], height=obj["height"])
            self.objects[i] = sge.dsp.Object(obj["x"], obj["y"], z=obj["layer"])
            i += 1


    def loadRoom(self):
        print("placeholder!")
        rObj = self.json_data[len(self.json_data)-1]
        self.intromusic = rObj["intromusic"]
        self.intromovie = rObj["intromovie"]
        #return sge.dsp.Room(objects=self.objects,
        #The following doesn't work, although I wish it would.  Pending a re-write
        #return CustomRoom(objects=self.objects,
         #intromusic=sge.snd.Sound(intromusic), intromovie=intromovie, music=None, background=sge.gfx.Background([], sge.gfx.Color("black")))
Game()
test = TestObject()
g = Generator("test/test.json")
g.createObjects()
objects = [test]
background = sge.gfx.Background([], sge.gfx.Color("white"))
#sge.game.start_room = sge.dsp.Room(objects=objects, background=background)
#print(isinstance(g.loadRoom(), sge.dsp.Room))
sge.game.start_room = g.loadRoom()
print("Current Room: " + str(sge.game.start_room))

if __name__ == '__main__':
    sge.game.start()
