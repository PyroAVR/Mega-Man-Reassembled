import sge

positive = ['yes', 'y', 'Y']
negative = ['no', 'n', 'N']

class Game(sge.dsp.Game):
    def __init__(self, height=640, width=960):
        super().__init__(width=width, height=height, window_text="Playground")
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


class REPL_Obj(sge.dsp.Object):
    def __init__(self, x, y, visible=False):
        print("Starting REPL")
        super().__init__(x, y, visible=visible)

    def event_key_press(self, key, char):
        com = input(":")
        if com == "exit":
            sge.game.end()
        if com == "add object":
            sdir = input("sprite dir:")
            sname = input("sprite fname:")
            xps = input("x position:")
            yps = input("y position:")

            if input("static?:") in negative:
                xvel = input("vx?:")
                yvel = input("vy?:")

                if input("physiscs?") in positive:
                    xacc = input("d2x:")
                    yacc = input("grav?:")
                    sge.game.current_room.add(sge.dsp.Object(int(xps),int(yps),
                    xvelocity=float(xvel), yvelocity=-float(yvel),
                    xacceleration=float(xacc), yacceleration=-float(yacc),
                    sprite=sge.gfx.Sprite(name=sname, directory=sdir)))
                    return 0

                sge.game.current_room.add(sge.dsp.Object(int(xps),int(yps),
                xvelocity=float(xvel), yvelocity=-float(yvel),
                sprite=sge.gfx.Sprite(name=sname, directory=sdir)))
                return 0

            sge.game.current_room.add(sge.dsp.Object(int(xps),int(yps),
            sprite=sge.gfx.Sprite(name=sname, directory=sdir)))
            return 0


class Playground:
    def __init__(self):
        Game()
        background = sge.gfx.Background([], sge.gfx.Color("white"))
        repl_obj = REPL_Obj(0,0)
        self.playground = sge.dsp.Room(objects=[repl_obj],background=background)
        sge.game.start_room = self.playground

    def start(self):
        print("Starting Playground")

        sge.game.start()





if __name__ == '__main__':
    p = Playground()
    p.start()
