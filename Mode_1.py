import pyttsx
import requests
import json
import os
from gtts import gTTS
# import vlc
import pyglet
import pyowm

class Mode_1:
	def __init__(self):
		print('Mode 1 initiated')
		self.engine = pyttsx.init()
		self.owm = pyowm.OWM('f81b4b9735f0c61ec1f31d704b621479')
		self.weather = self.owm.weather_at_place('Grand Rapids, us')

	def button_3(self, is_on):
		if is_on:
			self.greeting()
		else:
			self.goodbye()

	def button_4(self, is_on):
		print('mode 1 button 4')
		currWeather = self.weather.get_weather()
		print currWeather

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
		os.remove("good.mp3")
		os.system('cvlc --play-and-exit' + 'good.mp3')


	def goodbye(self):
		self.engine.say("Goodbye Ben")
		self.engine.runAndWait()
