"""
Facade provide a simplified interface to it's set of interfaces.
Advantages:
1. Client gain simplicity and subsystem get flexibility.
2. Reduce dependency to external code which it related to facade code but unrelated to client code.
3. Provides a better and clearer API for the client code.
"""
from __future__ import print_function, unicode_literals

from functools import reduce
from urllib.request import urlopen, URLError, quote
import httplib2
import json
import pickle
from datetime import timedelta, datetime


class WeatherProvider(object):
    def __init__(self):
        self.api_url = 'http://api.openweathermap.org/data/2.5/forecast?q=' \
                       '{},{}' \
                       '&appid=211d5e0dea27ca83eefcea0790126b1a'
        self.http = httplib2.Http()

    def get_weather_data(self, city, country):
        city = quote(city)
        url = self.api_url.format(city, country)
        # status, content = self.http.request(url)
        try:
            return urlopen(url).read()
        except URLError as e:
            return None


class Parser(object):
    def parse_weather_data(self, weather_data):
        parsed_data = json.load(weather_data)
        start_date = None
        results = []

        for item in parsed_data["lists"]:
            date = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
            start_date = start_date or date
            if start_date.day != date.day:
                return results
            results.append(item['main']['temp'])


class Converter(object):
    def kelvin_to_celcius(self, temp):
        return int(temp) - 273.15


class CachedObject(object):
    """
    Cached object that need to be saved in file
    """
    def __init__(self, obj, interval=1):
        self.obj = obj
        self.expired = datetime.utcnow() + timedelta(hours=interval)

    def __str__(self):
        pass


class Cache(object):
    def __init__(self, filename):
        self.filename = filename

    def save(self, obj):
        with open(self.filename, 'w') as file:
            dct = CachedObject(obj, 3)
            pickle.dump(dct, file)

    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                result = pickle.load(file)
                if result['expired'] > datetime.utcnow():
                    return result
        except IOError:
            pass


class Weather(object):
    """
    It receives an iterable of weather forecast for a day and calculates the median forecast:
    """
    def __init__(self, data):
        result = reduce(lambda x, y: x+y, data)
        self.temperature = result / len(data)


class Facade(object):
    """
    Facade class that provide a simple interface to weather subsystem:
    Cache, Converter, Parser and WeatherProvider object
    """
    def get_forcast(self, city, country):
        cache = Cache('myfile')
        cache_result = cache.load()
        if cache_result:
            return cache_result
        else:
            weather_provider = WeatherProvider()
            weather_data = weather_provider.get_weather_data(city, country)
            parser = Parser()
            parsed_data = parser.parse_weather_data(weather_data)
            weather = Weather(parsed_data)
            converter = Converter()
            temperature_celcius = converter.from_kelvin_to_celcius(weather.temperature)
            cache.save(temperature_celcius)
            return temperature_celcius

if __name__ == '__main__':
    facade = Facade()
    city = input("Enter you city: ")
    country = input("Enter you country: ")
    print(facade.get_forcast(city, country))