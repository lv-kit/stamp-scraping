import json
import urllib.request
from bs4 import BeautifulSoup

url = "https://ja.wikipedia.org/wiki/Unicode%E3%81%AEEmoji%E3%81%AE%E4%B8%80%E8%A6%A7"

instance = urllib.request.urlopen(url)

soup = BeautifulSoup(instance, "html.parser")

table = soup.select(".wikitable > tbody")
tableRow = table[0].find_all("tr")

ys = []

for i in range(len(tableRow)-1):
    i = i + 1
    data = {}
    data["model"] = "posts.stamps"
    data["pk"] = i
    data["name"] = tableRow[i].select_one('td:nth-of-type(3)').get_text().replace('\n', '')
    data["unicode"] = tableRow[i].select_one('td:nth-of-type(2)').get_text().replace('U+', '')
    data["fields"] = {"name": data["name"], "unicode": data["unicode"]}
    del data["name"]
    del data["unicode"]

    ys.append(data)

jsonFile = open("stamp1.json", "wt", encoding="utf-8")
json.dump(ys, jsonFile, indent=4)
