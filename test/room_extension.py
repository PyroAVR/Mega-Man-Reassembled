import sge

class RoomB(sge.dsp.Room):
    def event_room_start(self):
        s = sge.snd.Sound("assets/music/mmstart.ogg")
        s.play()
