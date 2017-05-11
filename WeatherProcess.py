import sched
import pyowm
import datetime
import os
from gtts import gTTS
import threading


class WeatherProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # Create a Temp directory if one does not currently exist
        if not os.path.exists("temp"):
            os.makedirs("temp")

    def run(self):
        self.owm = pyowm.OWM('f81b4b9735f0c61ec1f31d704b621479')
        self.semaphore = threading.Semaphore()
        self.pull_weather()


    def pull_weather(self):
        self.semaphore.acquire()
        currentWeather = self.owm.weather_at_place('Grand Rapids, us').get_weather()
        self.currentTemperature = currentWeather.get_temperature('fahrenheit')['temp']
        self.currentStatus = currentWeather.get_detailed_status()
        forecast = self.owm.daily_forecast('Grand Rapids, us, limit=7')
        tomorrowTime = pyowm.timeutils.tomorrow()
        tomorrowForcast = forecast.get_weather_at(tomorrowTime)
        self.tomorrowStatus = tomorrowForcast.get_detailed_status()
        self.tomorrowLow = tomorrowForcast.get_temperature('fahrenheit')['min']
        self.tomorrowHigh = tomorrowForcast.get_temperature('fahrenheit')['max']
        self.createAudio()

    def createAudio(self):
        #Create error message
        tts = gTTS(text='Sorry, updating the weather. Try again', lang = 'en')
        tts.save("temp/errorStatus.mp3")

        tts = gTTS(text='Tomorrow will have a high of ' + str(self.tomorrowHigh) + 'degrees and a low of ' + str(self.tomorrowLow), lang='en')
        tts.save("temp/tomorrowForecast.mp3")

        tts = gTTS(text="It is currently " + str(self.currentStatus) + "outside", lang = "en")
        tts.save("temp/currentStatus.mp3")
        self.semaphore.release()

        # tts = gTTS(text='', lang = 'en')
        # tts.save("temp/.mp3")
        #
        # tts = gTTS(text='', lang = 'en')
        # tts.save("temp/.mp3")
