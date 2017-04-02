#!/usr/local/bin/python3
# lolcat.py
# uses api call to get 8 random funny cat pictures and displays them to user

import requests
import os
import shutil
import subprocess
from sys import platform, argv

def print_header():
	print('-'*40)
	print("\tRANDOM LOL CAT APP")
	print('-'*40 + "\n")

def get_cat(folder, name):
	url = r"http://consuming-python-services-api.azurewebsites.net/cats/random"
	data = get_data_from_url(url)
	save_image(folder, name, data)

def get_data_from_url(url):
	response = requests.get(url, stream=True)
	return response.raw

def save_image(folder, name, data):
	file_name = os.path.join(folder, name + '.jpg')
	with open(file_name, 'wb') as fout:
		shutil.copyfileobj(data, fout)

if __name__ == '__main__':
	folder = argv[1] if len(argv) > 1 else '.'
	print_header()
	print("Contacting cat service for funny cat pictures ...")
	for x in range(1,8):
		print("Downloading Cat {} ....".format(x))
		get_cat(folder, "lolcat{}".format(x))
	if platform.startswith("linux"):
		print("Opening folder {} in files".format(folder))
		subprocess.call(['xdg-open', folder])
	elif platform.startswith("win32"):
		print("opening folder {} in explorer".format(folder))
		subprocess.call(['explorer', folder])
	elif platform.startswith("darwin"):
		print("opening folder {} in finder".format(folder))
		subprocess.call(['open', folder])
	else:
		print("Unsupported platform {}".format(str(platform)))