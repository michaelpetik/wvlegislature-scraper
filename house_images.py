import requests
import urllib, urlparse
from bs4 import BeautifulSoup
import os

url = "http://www.wvlegislature.gov/House/roster.cfm"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")
arr = ['members', 'house']

for link in soup.find_all('img'):
	image = link.get("src")
	if all(c in image for c in arr):
		image_fullurl = image.replace('../../','http://www.wvlegislature.gov/')
		split = urlparse.urlsplit(image_fullurl)
		filename = "house/members/images/" + split.path.split("/")[-1]
		urllib.urlretrieve(image_fullurl, filename)