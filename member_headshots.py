import requests
import urllib
from bs4 import BeautifulSoup
from datetime import datetime
import os

chambers = ["House", "Senate"]

for chamber in chambers:
    if chamber == "House":
        selected_chamber = ["House", "house"]
    if chamber == "Senate":
        selected_chamber = ["Senate1", "senate"]
    print(f'Retrieving information for current members of the {chamber}')

    url = f"http://www.wvlegislature.gov/{selected_chamber[0]}/roster.cfm"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    image_dir = f"{str(datetime.now().year)}/{selected_chamber[1]}/members/headshots/"
    
    if os.path.isdir(image_dir) == True:
        print("Data for this year has already been collected.")
        quit()
    else:    
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
