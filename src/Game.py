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
