import threading
import playsound

class AudioThread(threading.Thread):

    def __init__(self, audioName):
        threading.Thread.__init__(self)
        self.audioName = audioName

    def run(self):
        print(self.audioName)
        playsound.playsound(self.audioName, True)
