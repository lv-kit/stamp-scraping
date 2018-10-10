import json
import array
import collections as cl
import urllib.request
from bs4 import BeautifulSoup

url = "https://ja.wikipedia.org/wiki/Unicode%E3%81%AEEmoji%E3%81%AE%E4%B8%80%E8%A6%A7"

instance = urllib.request.urlopen(url)

soup = BeautifulSoup(instance, "html.parser")

table = soup.select(".wikitable > tbody")
# print(table)
tableRow = table[0].find_all("tr")

ys = cl.OrderedDict()

length = len(tableRow)

# print(length)

for i in range(len(tableRow)-1):
    i = i + 1
    data = {}
    data["model"] = "posts.stamps"
    data["pk"] = i
    data["name"] = tableRow[i].select_one('td:nth-of-type(3)').get_text()
    data["unicode"] = tableRow[i].select_one('td:nth-of-type(2)').get_text()
    data["fields"] = [data["name"], data["unicode"]]
    del data["name"]
    del data["unicode"]

    # print(ys)
    # print(data)

    ys[i] = data

# print(ys)
list_data = list(ys.items())

print(list_data)

jsonFile = open("stamp.json", "wt", encoding="utf-8")
json.dump(ys, jsonFile, indent=4)
# writer = json.writer(jsonFile)