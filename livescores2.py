import requests
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
           team1  = teamDiv.text.strip()
        else:
           team2  = teamDiv.text.strip()

    print(clockDiv.text.strip() + " : "+ team1 + "-" + scoreT1 + " X "  + scoreT2 + "-" + team2)
