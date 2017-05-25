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
    scores = scoreDiv.text.replace(" ", "").split("-")
    scoreT1 = scores[0]
    scoreT2 = scores[1]
    clockDiv = matchDiv.find('div', class_="min")
    for teamDiv in teamDivs:
    	if 'tright' in teamDiv.attrs['class']:
           t1  = teamDiv
        else:
           t2  = teamDiv

    print(clockDiv.text.strip() + " : "+ t1.text.strip() + "-" + scoreT1 + " X "  + scoreT2 + "-" + t2.text.strip())
    
    #t2 = matchDiv.find('div', class_="tright"
    #print(t1)
    #print(t2)
    
    #score = matchDiv.find('div',class_='score')
    #print(str(t1) + " " + str(score) + " " + str(t2))
    