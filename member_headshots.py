import requests
import urllib
from bs4 import BeautifulSoup
import os

while True:
    chamber = input("House or Senate?").lower()[0]

    if chamber == "s":
        selected_chamber = ["Senate1", "senate"]
        break
    elif chamber == "h":
        selected_chamber = ["House", "house"]
        break
    else:
        print("Invalid selection, please try again.")
        continue

url = f"http://www.wvlegislature.gov/{selected_chamber[0]}/roster.cfm"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")
image_dir = f"{selected_chamber[1]}/members/headshots/"

if os.path.isdir(image_dir) == False:
    os.makedirs(image_dir)

for link in soup.find_all('img'):
    image = link.get("src")
    if "members" in image:
        image_fullurl = image.replace(
            '../../', 'http://www.wvlegislature.gov/')
        split = urllib.parse.urlsplit(image_fullurl)
        filename = image_dir + split.path.split("/")[-1]
        print(image_fullurl)
        urllib.request.urlretrieve(image_fullurl, filename)
