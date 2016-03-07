import sge
background = sge.gfx.Background([], sge.gfx.Color("white"))
class Menu(sge.dsp.Room):
    def event_step(self, time_passed, delta_mult):
        font = sge.gfx.Font("assets/Fonts/PressStart2P.ttf",size=24)
        sge.game.project_text(font, "Hello, World!", sge.game.width/2, sge.game.height/2, color=sge.gfx.Color("gray"), halign="center", valign="middle")
