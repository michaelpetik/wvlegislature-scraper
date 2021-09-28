import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
import os

while True:
	year = int(eval(input("Year?")))

	if year < 1993:
		print("Pre-1993 data unavailable. Please try a more recent year.")
		continue	
	elif year > int(datetime.now().year):
		print("What are ya, some kind of time traveler? Try a year that's already happened.")
		continue
	else:
		break

while True:
    chamber = input("House or Senate?").lower()[0]

    if chamber == "s":
        selected_chamber = ["s", "senate"]
        break
    elif chamber == "h":
        selected_chamber = ["h", "house"]
        break
    else:
        print("Invalid selection, please try again.")
        continue


url = f'http://www.wvlegislature.gov/Bill_Status/Bills_all_bills.cfm?year={year}&sessiontype=rs&btype=bill&orig={selected_chamber[0]}'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
bill_list = []
data_dir = f"{str(year)}/{selected_chamber[1]}/billstatus/"
data_file = str(data_dir + "billstatus.json")

if os.path.isdir(data_dir) == False:
    os.makedirs(data_dir)

if os.path.isfile(data_file) == True:
    print("Data for this year has already been collected.")
    quit()
else:
    for table_row in soup.select("table.tabborder tr"):
        cells = table_row.findAll('td')
        if len(cells) == 6:
            bill_number = cells[0].text.strip()
            bill_title = cells[1].text.strip()
            bill_status = cells[2].text.strip()
            bill_committee = cells[3].text.strip()
            bill_step = cells[4].text.strip()
            last_action = cells[5].text.strip()
    
            bill_info = {"bill_number": bill_number, "bill_title": bill_title, "bill_status": bill_status,
                         "bill_committee": bill_committee, "bill_step": bill_step, "last_action": last_action}
            bill_list.append(bill_info)
    
        if len(cells) == 5:
            bill_number = cells[0].text.strip()
            bill_title = cells[1].text.strip()
            bill_status = cells[2].text.strip()
            bill_step = cells[3].text.strip()
            last_action = cells[4].text.strip()
    
            bill_info = {"bill_number": bill_number, "bill_title": bill_title,
                         "bill_status": bill_status, "bill_step": bill_step, "last_action": last_action}
            bill_list.append(bill_info)
    
        if len(cells) == 4:
            bill_number = cells[0].text.strip()
            bill_title = cells[1].text.strip()
            bill_status = cells[2].text.strip()
            last_action = cells[3].text.strip()
    
            bill_info = {"bill_number": bill_number, "bill_title": bill_title,
                         "bill_status": bill_status, "last_action": last_action}
            bill_list.append(bill_info)
    
    billstatus_json = json.dumps(bill_list)
    
    with open(data_file, 'a') as outfile:
        outfile.write(billstatus_json)