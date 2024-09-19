#!/usr/bin/env python
import requests


def download(url):
	get_respone = requests.get(url)
	print(get_respone.content)
	with open ("sample.txt", "w") as out_file:
		out_file.write("I LOVE YOU")
download("https://www.bleepstatic.com/content/hl-images/2021/07/29/NSA.jpg")