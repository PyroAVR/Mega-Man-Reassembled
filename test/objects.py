import sge
import xsge_tmx as xtmx
import os
from DialogBox import DialogBox
from room_extension import RoomB

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
#please rename this
class ExtendedRoom(sge.dsp.Room):
    #using this instead of overloading __init__
    #load objects outside of this, this should be fast, does not load automatically.
    def setup_custom_objects(self, intromusic=None, intromovie=None, music=None):
        self.intromusic = intromusic
        self.intromovie = intromovie
        self.music = music

    def event_room_start(self):
        print("placeholder")
        self.intromusic.play()



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

    def loadObjects(self):
        i = 0
        for obj in self.json_data:
            #Do not read the last element.  That is the room descriptor.
            if i == self.json_num_elements -1:
                return

            if obj["type"] == "AIObject":
                print("Type is Computer Player")
            elif obj["type"] == "Player":
                print("Type is Human Player.  Registering new player...")
            elif obj["type"] == "DialogBox":
                print("Type is DialogBox.  Registering new DialogBox id...")
            #how big is the path name?
            sizeof_path = len(obj["sprite"])
            sp_string = obj["sprite"]
            #Where's the last '/' in the sprite field?
            delim = sp_string.rfind("/") +1
            sprite_path = sp_string[0:delim]
            sprite_name = sp_string[delim:sizeof_path]
            #print(sprite_path)
            #print(sprite_name)
            #print(obj["x"])
            s = sge.gfx.Sprite(name=sprite_name, directory=sprite_path, width=obj["width"], height=obj["height"])
            self.objects[i] = sge.dsp.Object(obj["x"], obj["y"], z=obj["layer"])
            i += 1


    def loadRoom(self):
        print("placeholder!")
        rObj = self.json_data[len(self.json_data)-1]
        self.Room = xtmx.load(rObj["tmx"], cls=ExtendedRoom)
        #Eventually, intromovie/music will be supported.
        self.Room.setup_custom_objects(intromusic=sge.snd.Music(rObj["intro_music"]), music=sge.snd.Music(rObj["music"]))
        return self.Room


Game()
test = TestObject()
g = Generator("test/test.json")
objects = [test]
r = RoomB()
background = sge.gfx.Background([], sge.gfx.Color("white"))
#sge.game.start_room = sge.dsp.Room(objects=objects, background=background)
#print(isinstance(g.loadRoom(), sge.dsp.Room))
r = g.loadRoom()
#print("r = " + str(r))
sge.game.start_room = r
#sge.game.start_room = xtmx.load("assets/lvl.tmx", cls=ExtendedRoom)
#print("Current Room: " + str(sge.game.start_room))
if __name__ == '__main__':
    sge.game.start()
