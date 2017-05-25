import requests
import csv
from BeautifulSoup import BeautifulSoup

url = url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class' : 'stripe'})

rowsList = []
for row in table.findAll('tr'):
  cellsList = []
  for cell in row.findAll('td'):
    text = cell.text.replace('&nbsp;', '')
    cellsList.append(text)
  rowsList.append(cellsList)

outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(rowsList)