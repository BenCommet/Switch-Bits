import pyttsx
import os
from gtts import gTTS
import pyowm
from WeatherProcess import WeatherProcess
from AudioThread import AudioThread

class Mode_1:
	def __init__(self, weather):
		print('Mode 1 initiated')
		self.weatherProcess = weather

	def button_3(self, is_on):
		if is_on:
			self.weatherProcess.semaphore.acquire()
			audioThread = AudioThread("temp/currentStatus.mp3")
			audioThread.setDaemon(True)
			audioThread.start()
			self.weatherProcess.semaphore.release()

	def button_4(self, is_on):
		print('mode 1 button 4')
		if is_on:
			self.weatherProcess.semaphore.acquire()
			audioThread = AudioThread("temp/tomorrowForecast.mp3")
			audioThread.setDaemon(True)
			audioThread.start()
			self.weatherProcess.semaphore.release()
	def button_5(self, s_on):
		print('mode 1 button 5')

	def button_6(self, is_on):
		print('mode 1 button 6')

	def button_7(self, is_on):
		print('mode 1 button 7')

	def button_8(self, is_on):
		print('mode 1 button 8')

	def stop(self):
		print("stopping mode 1")

	def greeting(self):
		# self.engine.say("Hello Ben")
		# self.engine.runAndWait()
		tts = gTTS(text='Good morning Sir Benjamin Commet, Esteemed Knight of the land and all around awesome fella', lang='en')
		tts.save("good.mp3")
		audio = pyglet.media.load("good.mp3", streaming=False)
		audio.play()


	def goodbye(self):
		self.engine.say("Goodbye Ben")
		self.engine.runAndWait()
