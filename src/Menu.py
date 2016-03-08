import sge
from DialogBox import DialogBox
background = sge.gfx.Background([], sge.gfx.Color("white"))
class Menu(sge.dsp.Room):
    def event_step(self, time_passed, delta_mult):
        font = sge.gfx.Font("assets/Fonts/PressStart2P.ttf",size=24)
        sge.game.project_text(font, "Megaman", sge.game.width/2, sge.game.height/4, color=sge.gfx.Color("blue"), halign="center", valign="middle")
        sge.game.project_text(font, "REASSEMBLED", sge.game.width/2, (sge.game.height/4)+100, color=sge.gfx.Color("red"), halign="center", valign="middle")
        b = DialogBox(None, None, None)
