import sge

class DialogBox(sge.dsp.Object):
    def __init__(self, char_sprite, font, text):
        self.text = text
        self.font = font
        self.box_width   =   sge.game.width/(1.618*6)
        self.box_height  =   sge.game.height/(1.618*6)
        self.font_size   =   12 #Don't change this until scaling works
        self.char_sprite =   char_sprite
        self.master_sprite = sge.gfx.Sprite(width=self.box_width, height=self.box_height)

#        self.upper_left     =   sge.gfx.Sprite("assets/uitiles/ul.png", width=32, height=32)
#        self.lower_left     =   sge.gfx.Sprite("assets/uitiles/ll.png", width=32, height=32)
#        self.upper_right    =   sge.gfx.Sprite("assets/uitiles/ur.png", width=32, height=32)
#        self.lower_right    =   sge.gfx.Sprite("assets/uitiles/lr.png", width=32, height=32)

#    def event_step(self, time_passed, delta_mult):
    #Change what to say
    def change_text(self, new_text):
        self.text = new_text

    #Change the font used to print
    def change_font(self, new_font):
        self.font = new_font

    #Change the sprite for who is "speaking"
    def change_char(self, new_char):
        self.char_sprite = new_char

    #Render the sprite.  Should be internalized
    def render(self):
        self.master_sprite.draw_text(font=self.font, text=self.text, color=sge.gfx.Color("red"), x=0, y=0, frame=None)
        super().__init__(self.box_width, sge.game.height, sprite=self.master_sprite)
