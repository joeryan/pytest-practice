#!/usr/bin/python
# weather.py
# a simple app that gets the weather for a zip code entered at command line
import re
import requests


print('-'*40)
print("\tWEATHER CLIENT APP")
print('-'*40 + "\n")

baseURL = r"http://api.openweathermap.org/data/2.5/weather"
zipmatcher = re.compile(r"[0-9]{5}")
selection = ''

while selection.lower() != 'q':
	selection = input("Enter your zipcode (e.g. 94101): ")
	zipcode = zipmatcher.match(selection)
	if not zipcode:
		continue
	zipcode = zipcode.group(0)
	print("The weather in {z} is ...".format(z=zipcode))
