import requests
from bs4 import BeautifulSoup
import csv

page_scraped = requests.get("https://top100.indianapolis.iu.edu/about/past-recipients/#past", verify=False)

soup = BeautifulSoup(page_scraped.text, "html.parser")

names = soup.find_all("tr")

file = open("top100.csv", "w")
writer = csv.writer(file)

writer.writerow(["Name", "School"])

for name in names:
    tds = name.find_all("td")
    td_texts = [td.get_text(strip=True) for td in tds]
    print(" - ".join(td_texts))
    writer.writerow(td_texts)
file.close()
