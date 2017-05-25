import requests
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://www.flashscore.com/soccer/'
url2 = "http://www.xscores.com/soccer/livescores/25-05"
response = requests.get(url2)
html = response.content

soup = BeautifulSoup(html)
with open("xshtml.html", "w") as file:
    file.write(str(soup))