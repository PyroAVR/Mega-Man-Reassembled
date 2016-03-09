import sge
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


class Generator:
    def __init__(self, filename):
        import json     #this screams bad practice to me
        self.raw_data = ''
        with open(filename, 'r') as file:   #with is one of Python's saving graces
            self.raw_data = file.read()
        self.json_obj = json.loads(self.raw_data)
        print(self.json_obj["2"])
    def get_obj
Game()
test = TestObject()
g = Generator("test/test.json")
objects = [test]
background = sge.gfx.Background([], sge.gfx.Color("white"))
sge.game.start_room = sge.dsp.Room(objects, background=background)


if __name__ == '__main__':
    sge.game.start()
