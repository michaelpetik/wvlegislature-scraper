import requests
from bs4 import BeautifulSoup

url = 'http://www.wvlegislature.gov/Bill_Status/Bills_all_bills.cfm?year=2018&sessiontype=rs&btype=bill&orig=h'

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

bill_list = []

for table_row in soup.select("table.tabborder tr"):
	cells = table_row.findAll('td')
	if len(cells) == 6:
		bill_number = cells[0].text.strip()
		bill_title = cells[1].text.strip()
		bill_status = cells[2].text.strip()
		bill_committee = cells[3].text.strip()
		bill_step = cells[4].text.strip()
		last_action = cells[5].text.strip()

		bill_info = {'bill_number': bill_number, 'bill_title': bill_title, 'bill_status': bill_status, 'bill_committee': bill_committee, 'bill_step': bill_step, 'last_action': last_action}
		bill_list.append(bill_info)

		print "{0} | {1} | {2} | {3} | {4} | {5}".format(bill_number, bill_title, bill_status, bill_committee, bill_step, last_action)

	if len(cells) == 5:
		bill_number = cells[0].text.strip()
		bill_title = cells[1].text.strip()
		bill_status = cells[2].text.strip()
		bill_step = cells[3].text.strip()
		last_action = cells[4].text.strip()

		bill_info = {'bill_number': bill_number, 'bill_title': bill_title, 'bill_status': bill_status, 'bill_step': bill_step, 'last_action': last_action}
		bill_list.append(bill_info)

		print "{0} | {1} | {2} | {3} | {4}".format(bill_number, bill_title, bill_status, bill_step, last_action)

	if len(cells) == 4:
 		bill_number = cells[0].text.strip()
 		bill_title = cells[1].text.strip()
 		bill_status = cells[2].text.strip()
 		last_action = cells[3].text.strip()

		bill_info = {'bill_number': bill_number, 'bill_title': bill_title, 'bill_status': bill_status, 'last_action': last_action}
		bill_list.append(bill_info)

		print "{0} | {1} | {2} | {3}".format(bill_number, bill_title, bill_status, last_action)
