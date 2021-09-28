import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
import os

active_year = 1993
current_year = int(datetime.now().year)
chambers = ["House", "Senate"]

while active_year <= current_year:
    for chamber in chambers:   
        print(f'Retrieving data for the {chamber} in {str(active_year)}')

        url = f'http://www.wvlegislature.gov/Bill_Status/Bills_all_bills.cfm?year={active_year}&sessiontype=rs&btype=bill&orig={chamber.lower()[:1]}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        bill_list = []
        data_dir = f"{str(active_year)}/{chamber.lower()}/billstatus/"
        data_file = str(data_dir + "billstatus.json")

        if os.path.isdir(data_dir) == False:
            os.makedirs(data_dir)

        if os.path.isfile(data_file) == True:
            print("Data for this year has already been collected.")
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

    active_year = active_year + 1
