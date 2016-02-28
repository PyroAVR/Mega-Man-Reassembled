import sge

class Menu(sge.dsp.Room):
    def event_step(self, time_passed, delta_mult):
        font = sge.gfx.Font()
        sge.game.project_text(font, "Hello, World!", sge.game.width/2, sge.game.height/2, color=sge.gfx.Color("black"), halign="center", valign="middle")
