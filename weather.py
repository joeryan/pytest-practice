#!/usr/bin/python
# weather.py
# a simple app that gets the weather for a zip code entered at command line
import re
import requests
from os import environ as env


print('-'*40)
print("\tWEATHER CLIENT APP")
print('-'*40 + "\n")

apiKey = env['OWM_KEY'] if 'OWM_KEY' in env.keys() else ""
baseURL = r"http://api.openweathermap.org/data/2.5/weather"
zipmatcher = re.compile(r"[0-9]{5}")
selection = ''

while selection.lower() != 'q':
	selection = input("Enter your zipcode (e.g. 94101): ")
	zipcode = zipmatcher.match(selection)
	if not zipcode:
		continue
	zipcode = str(zipcode.group(0))+",us"
	parameters = {'zip': zipcode, 'APPID': apiKey}
	response = requests.get(baseURL, params=parameters)
	print(response.status_code)
	print("The weather in {z} is ...".format(z=zipcode))
