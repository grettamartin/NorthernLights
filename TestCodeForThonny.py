from bs4 import BeautifulSoup

import requests

pageToScrape = requests.get("https://www.swpc.noaa.gov/products/planetary-k-index#")
soup = BeautifulSoup(pageToScrape.text, "html.parser")
spanContent = soup.findAll("span")
#print(spanContent)
for span in spanContent:
    if "Estimated Planetary K index" in span.text:
        kpIndex = span.text
        kpIndex = kpIndex.split(":")[-1].strip()
        print(kpIndex)
print(spanContent)

