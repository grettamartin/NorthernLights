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

#checks if cme has been detected within past 48 hours
cme_II_presence = "false"
cme_III_presence = "false"
cme_IV_presence = "false"

text_url = "https://www.sidc.be/cactus/out/cmecat.txt"
response = requests.get(text_url)

content = response.text
lines = content.splitlines()

date_list = [] #index 0
da_list = [] #index

line_count = 0
for line in lines:
    line_count += 1
    if (line_count >= 28) and (line_count <= 50) :
        #print(line[2])
        split_line = line.split('|')
        date = split_line[1].strip()
        date_list.append(date)
        da = split_line[4].strip()
        da_list.append(da)
 
da_index = 0
for da in da_list:
    int_da = int(da)
    da_index +=0
    if int_da > 270:
        cme_IV_presence = "true"
    elif int_da > 180:
        cme_III_presence = "true"
    elif int_da > 90:
        cme_II_presence = "true"

if cme_IV_presence == "true":
    print("There has recently been a coronal mass ejection with a type IV halo.")
if cme_III_presence == "true":
    print("There has recently been a coronal mass ejection with a type III halo.")
if cme_II_presence == "true":
    print("There has recently been a coronal mass ejection with a type II halo.")

