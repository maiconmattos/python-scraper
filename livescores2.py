import requests
import csv
from bs4 import BeautifulSoup

url = "http://livescores.com"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
matchDivs = soup.find_all('div', class_='row-gray')
for matchDiv in matchDivs :
    teamDivs = matchDiv.findAll('div', class_="ply")
    t1 = ''
    t2 = ''
    scoreDiv = matchDiv.find('div', class_="sco")
    for teamDiv in teamDivs:
    	if 'tright' in teamDiv.attrs['class']:
           t1  = teamDiv
        else:
           t2  = teamDiv

    print(t1.text + " " + scoreDiv.text + " " + t2.text)
    
    #t2 = matchDiv.find('div', class_="tright"
    #print(t1)
    #print(t2)
    
    #score = matchDiv.find('div',class_='score')
    #print(str(t1) + " " + str(score) + " " + str(t2))
    