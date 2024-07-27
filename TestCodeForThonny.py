#from bs4 import BeautifulSoup

import requests

json_url = "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json"

pageToScrape = requests.get(json_url)
raw_data = pageToScrape.json()

headers = raw_data[0]
rows = raw_data[1:]

print(headers)
print(rows)

kp_index_position = headers.index("Kp")

size = 0
kpList = []

for row in rows:
    time_tag = row[0]
    kp_value = row[kp_index_position]
    size += 1
    kpList.append(kp_value)

current_kp = kpList[size-1]
print(current_kp)
    
    #print(time_tag, kp_value)

# spanContent = soup.findAll("span")
# #print(spanContent)
# for span in spanContent:
#     if "Estimated Planetary K index" in span.text:
#         kpIndex = span.text
#         kpIndex = kpIndex.split(":")[-1].strip()
#         print(kpIndex)
# print(spanContent)

