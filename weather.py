#!/usr/bin/python
# weather.py
# a simple app that gets the weather for a zip code entered at command line
import codecs
import json
import re
import requests

from os import environ as env

apiKey = env['OWM_KEY'] if 'OWM_KEY' in env.keys() else ""
baseURL = r"http://api.openweathermap.org/data/2.5/weather"
zipmatcher = re.compile(r"[0-9]{5}")

def printHeader():
	print('-'*40)
	print("\tWEATHER CLIENT APP")
	print('-'*40 + "\n")

def printError(response):
	print("Recieved status code: {0}".format(response.status_code))
	print(response.content)

def outputWeather(response):
	reader = codecs.getreader('utf-8')
	weather = json.loads(response.content)
	#print(json.dumps(weather, indent=4))
	print("The weather in {city} is {temp} degrees F with {wx}".format(city=weather["name"],
				temp=weather["main"]["temp"], wx=weather["weather"][0]["description"]))

def getWeather(zipcode):
	zipcode = str(zipcode.group(0))+",us"
	parameters = {'zip': zipcode, 'APPID': apiKey, 'units': 'imperial'}
	response = requests.get(baseURL, params=parameters)
	if (response.status_code == 200):
		outputWeather(response)
	else:
		printError(response)

if __name__ == '__main__':
	selection = ''
	while selection != 'q':
		selection = input("Enter your zipcode (e.g. 94101): ")
		zipcode = zipmatcher.match(selection)
		if zipcode:
			getWeather(zipcode)
