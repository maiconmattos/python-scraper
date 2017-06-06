import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.flashscore.com/soccer/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
with open("xshtml.html", "w") as f: f.write(str(soup))