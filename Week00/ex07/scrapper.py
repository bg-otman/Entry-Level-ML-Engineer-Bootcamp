import requests
import html5lib
from bs4 import BeautifulSoup

response = requests.get("https://data.1337ai.org/")

soup_html = BeautifulSoup(response.content, "html5lib")

table = soup_html.find("table")

file = open("data.csv", "w")

rows = table.find_all("tr")
for row in rows:
    columns = [column.get_text() for column in row]
    file.write(",".join(columns))
    file.write("\n")
print("data scrapped successfully and saved in data.csv")
file.close()
