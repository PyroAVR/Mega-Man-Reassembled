import sge
import xsge_gui

class DialogBox(sge.dsp.Object):
    def __init__(self, char_sprite, font, text):
        self.box_width   =   sge.game.width
        self.box_height  =   sge.game.height/(1.618*6)
        super().__init__(self.box_width, sge.game.height)
        self.upper_left     =   sge.gfx.Sprite("assets/uitiles/ul.png", width=32, height=32)
        self.lower_left     =   sge.gfx.Sprite("assets/uitiles/ll.png", width=32, height=32)
        self.upper_right    =   sge.gfx.Sprite("assets/uitiles/ur.png", width=32, height=32)
        self.lower_right    =   sge.gfx.Sprite("assets/uitiles/lr.png", width=32, height=32)
