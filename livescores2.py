import requests
from bs4 import BeautifulSoup
import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(): print "From print_time", time.time()

def scrapeResults() :
    print('  ')
    url = "http://livescores.com"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    matchDivs = soup.find_all('div', class_='row-gray')
    for matchDiv in matchDivs :
        clockDiv = matchDiv.find('div', class_="min")
        isLive = clockDiv.find('img')
        if isLive :
            clock = clockDiv.text.strip()
            scoreDiv = matchDiv.find('div', class_="sco")
            scores = scoreDiv.text.replace(" ", "").split("-")
            scoreT1 = scores[0]
            scoreT2 = scores[1]
            teamDivs = matchDiv.findAll('div', class_="ply")
            for teamDiv in teamDivs:
                if 'tright' in teamDiv.attrs['class']:team1 = teamDiv.text.strip()
            else: 
                team2 = teamDiv.text.strip()
            print(clock + " : " + team1 + "-" + scoreT1 + " vs " + scoreT2 + "-" + team2)
    print('-----------------------------')
    
scrapeResults()

while(True) :
    s.enter(60, 1, scrapeResults, ())
    s.run()