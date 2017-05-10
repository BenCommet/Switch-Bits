import sched
import pyowm
import datetime

class WeatherProcess:
    def __init__(self):
        self.owm = pyowm.OWM('f81b4b9735f0c61ec1f31d704b621479')
        self.pull_weather()

    def pull_weather(self):
        currentWeather = self.owm.weather_at_place('Grand Rapids, us').get_weather()
        self.currentTemperature = currentWeather.get_temperature('fahrenheit')['temp']
        self.currentStatus = currentWeather.get_detailed_status()
        forecast = self.owm.daily_forecast('Grand Rapids, us, limit=7')
        print(forecast)
        tomorrowTime = pyowm.timeutils.tomorrow()
        tomorrowForcast = forecast.get_weather_at(tomorrowTime)
        self.tomorrowStatus = tomorrowForcast.get_detailed_status()
        self.tomorrowLow = tomorrowForcast.get_temperature('fahrenheit')['min']
        self.tomorrowMax = tomorrowForcast.get_temperature('fahrenheit')['max']


        print(self.tomorrowStatus)
        print(self.tomorrowMax)
        # self.weatherTomorrow
