import tweepy
from tweepy import OAuthHandler
import json
 
consumer_key = 'N3bIWe0YODH0tiN1mBOvn1xU3'
consumer_secret = '3wKjm8FFZBY4JtJzyAaHkYcCdGLiOYPgGIFhiANLSVGp1lvf2b'
access_token = '874639429268381696-DkspeBInwdr3m1Bh5SsQnIbD1rAzVuh'
access_secret = 'tkYZUbFKzFVHUOQBj2sYWsUZMFrfDdTx40SEBMwSUipAE'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
print("Connected on twitter :" + str(api))

rate_limit = api.rate_limit_status()
print rate_limit['resources']['statuses']['/statuses/home_timeline']
print rate_limit['resources']['users']['/users/lookup']

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        text = (' '.join(status.text.split()) + " ")
        if (text.upper().find("SFC")>=0):
            if (text.upper().startswith('LATEST')):
                parse(text, 'LATEST')
            elif (text.upper().startswith('RESULT')):
                parse(text, 'RESULT')
            elif (text.upper().startswith('HALF-TIME') or text.upper().startswith('HALF TIME') or text.upper().startswith('HALFTIME')): 
                parse(text, 'HALF-TIME')
            elif (text.upper().startswith('FULL-TIME') or text.upper().startswith('FULL TIME') or text.upper().startswith('FULLTIME')): 
                parse(text, 'FULL-TIME')
    def on_error(self, status_code):
        if status_code == 420:
            print('Ooops! ' + str(status_code) + ' - Rate limit exceeded')
            return False
        else:
            print('Ooops! ' + str(status_code) + ' - Something went wrong')
            return False

def parse(text, event):
    print("---------------")
    print("TWEET : " + text)
    
    print("EVENT : " + event)
    
    time = text[ text.find("(") : (text.find(")") + 1) ]
    print("TIME : " + time)
    
    textFromTeam1Name = text[text.find("@"):]
    team1NameFinalPos = textFromTeam1Name.find(" ")
    team1Name = textFromTeam1Name[0:team1NameFinalPos]
    print ("TEAM1_NAME " + team1Name)

    textFromTeam1Score = textFromTeam1Name[team1NameFinalPos+1:]
    team1ScoreFinalPos = textFromTeam1Score.find(" ")
    team1Score = textFromTeam1Score[0:team1ScoreFinalPos]
    print ("TEAM1_SCORE " + team1Score)

    textFromTeam2Name = textFromTeam1Score[team1ScoreFinalPos+1:]
    team2NameFinalPos = textFromTeam2Name.find(" ")
    team2Name = textFromTeam2Name[0:team2NameFinalPos]
    print ("TEAM2_NAME " + team2Name)

    textFromTeam2Score = textFromTeam2Name[team2NameFinalPos+1:]
    team2ScoreFinalPos = textFromTeam2Score.find(" ")
    team2Score = textFromTeam2Score[0:team2ScoreFinalPos + 1]
    print ("TEAM2_SCORE " + team2Score)
    print("---------------")
    print(" ")

def start_stream():
    while True:
        try:
            myStreamListener = MyStreamListener
            myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())
            myStream.filter(follow=['89700550'])
        except: 
            continue

start_stream()


#843856454 - @mobstatsmob
#89700550 - @officialgaa
#874639429268381696 - @maiconmattos83

