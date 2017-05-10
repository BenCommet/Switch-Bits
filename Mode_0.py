import platform
import win32api
class Mode_0:
	def __init__(self):
		print('Mode 0 initiated')
		self.platform = platform.system()

	def button_3(self, is_on):
		print('mode 0 button 3 ' + str(is_on))
		print(self.platform)
		if self.platform == "Windows":
			self.playWindows()

	def button_4(self, is_on):
		print('mode 0 button 4 on: ' + str(is_on))
		if self.platform == "Windows":
			if(is_on):
				self.previousTrackWindows()

	def button_5(self, is_on):
		print('mode 0 button 5 on: ' + str(is_on))
		if self.platform == "Windows":
			if(is_on):
				self.nextTrackWindows()

	def button_6(self, is_on):
		print('mode 0 button 6 on: ' + str(is_on))
		if self.platform == "Windows":
			self.decreaseAudioWindows()

	def button_7(self, is_on):
		print('mode 0 button 7 on: ' + str(is_on))
		if self.platform == "Windows":
			self.increaseAudioWindows()

	def button_8(self, is_on):
		print('mode 0 button 8 on: ' + str(is_on))
		if self.platform == "Windows":
			self.muteAudioWindows()
	def stop(self):
		print("stopping mode 0")

	def reduceVolumeWindows(self):
		print('audioDown')

	def decreaseAudioWindows(self):
		print('volume down')
		decreaseVolumeKey = win32api.MapVirtualKey(0xAE, 0)
		win32api.keybd_event(0xAE, decreaseVolumeKey)

	def increaseAudioWindows(self):
		print('volume up')
		increaseVolumeKey = win32api.MapVirtualKey(0xAF, 0)
		win32api.keybd_event(0xAF, increaseVolumeKey)

	def muteAudioWindows(self):
		print('Mute')
		playButtonKey = win32api.MapVirtualKey(0xAD, 0)
		win32api.keybd_event(0xAD, playButtonKey)

	def playWindows(self):
		print('play/pause')
		playButtonKey = win32api.MapVirtualKey(0xB3, 0)
		win32api.keybd_event(0xb3, playButtonKey)

	def nextTrackWindows(self):
		print('next track')
		nextKey = win32api.MapVirtualKey(0xb0, 0)
		win32api.keybd_event(0xb0, nextKey)

	def previousTrackWindows(self):
		print('previous track')
		previousKey = win32api.MapVirtualKey(0xb1, 0)
		win32api.keybd_event(0xb1, previousKey)
