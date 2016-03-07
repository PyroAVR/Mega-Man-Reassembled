import sge

class Game(sge.dsp.Game):
    #def __init__(self):
        #super().__init__()
        #self.pauseSprite = sge.gfx.Sprite(height=1080, width=1920)
        #sge.game.mouse.visible = True;
    def event_key_press(self, key, char):
        if key == 'escape':
            self.event_close()
        elif key == 'f11':
            self.fullscreen = not self.fullscreen
        elif key == 'f8':
            sge.gfx.Sprite.from_screenshot().save("screenshot.png")
        elif key == 'p':
            self.pause()

    def event_close(self):
        self.end()

    def event_paused_key_press(self, key, char):
        if key == 'escape':
            self.event_close()
        else:
            self.unpause()
    def event_paused_close(self):
        self.event_close()
