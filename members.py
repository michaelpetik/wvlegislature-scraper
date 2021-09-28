import requests
from bs4 import BeautifulSoup

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

url = f'http://www.wvlegislature.gov/{selected_chamber[0]}/roster.cfm'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
bill_list = []

for table_row in soup.select("table.tabborder tr"):
    cells = table_row.findAll('td')
    if len(cells) == 6:
        member_name = cells[0].text.strip()
        member_party = cells[1].text.strip()
        member_district = cells[2].text.strip()
        member_address = cells[3].text.strip()
        member_email = cells[4].text.strip()
        member_phone = cells[5].text.strip()

        bill_info = {'member_name': member_name, 'member_party': member_party, 'member_district': member_district,
                     'member_address': member_address, 'member_email': member_email, 'member_phone': member_phone}
        bill_list.append(bill_info)

        print("{0},{1},{2},{3},{4},{5}".format(member_name, member_party,
              member_district, member_address, member_email, member_phone))
