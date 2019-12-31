import datetime
import json
import urllib.request
import requests

class ObtainWeatherInfo:

    def __init__(self):
        self.urltojson = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id=2720382&APPID=da5c9b841c0fbb4a1a8285a89c739cdb")
        self.response = self.urltojson.read()
        self.decodedResponse = self.response.decode("utf-8")
        self.jsondata = json.loads(self.decodedResponse)
        self.celsius = float(self.jsondata["main"]["temp"]) - 237.15

    def get_current_temp(self):
        return self.celsius