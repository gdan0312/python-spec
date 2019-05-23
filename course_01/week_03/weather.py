"""
Пример программы на использование классов
"""

import pprint

import requests
from dateutil.parser import parse

APP_ID = 'f95e1b4f1d25bfe2da004949d1c5c08b'


class CityInfo:
    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


class OpenWeatherForecast:
    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]

        url = 'http://api.openweathermap.org/data/2.5/forecast/' \
              '?q={city}&units=metric&cnt=3&mode=json&appid={APP_ID}'.format(city=city, APP_ID=APP_ID)
        print('sending HTTP request')
        response = requests.get(url).json()
        forecast = []
        for item in response['list']:
            forecast.append({
                'datetime': parse(item['dt_txt']),
                'temp_min': item['main']['temp_min'],
                'temp_max': item['main']['temp_max']
            })
        self._city_cache[city] = forecast
        return forecast


if __name__ == '__main__':
    weather_forecast = OpenWeatherForecast()
    for i in range(5):
        city_info = CityInfo('Novosibirsk', weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)

